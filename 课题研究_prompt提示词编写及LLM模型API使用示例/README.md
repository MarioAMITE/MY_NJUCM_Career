# 技术附件：基于 LLM Agent 的大规模转录组表型自动化整理工作流

**项目关联**：《基于基因表达特征的感染性疾病亚型分类模型研究》  
**核心贡献**：针对感染性疾病预后需求，构建自动化 Agent 管道，利用多 LLM 接口（DeepSeek/Qwen/ChatGPT）解析异构 SRA/GEO 元数据，完成 500+ 数据集、~70,000 样本、20,000 基因的**外周血转录组表型信息**结构化提取。

---

## 1. 系统架构与设计理念

本工作流摒弃传统人工查阅 SRA Run Selector 的方式，创新性地引入 **“LLM-as-Agent”** 策略，通过精心设计的 **Prompt 工程** 驱动大语言模型理解非结构化的 BioProject/GEO 文本，自动完成疾病分型（ICD-11）、样本分组、临床变量映射等复杂任务。

- **基础设施**：依托 **Linux 高性能计算集群**，使用 Slurm/PBS 任务调度。
- **核心工具链**：Python（数据抓取/LLM调度） + R（GEOquery/rentrez 深度挖掘） + Shell（管道胶水）。
- **LLM 集成**：统一封装兼容 OpenAI API 格式的接口，无缝切换 DeepSeek、ChatGPT 及 Qwen。

---

## 2. 模块化脚本详解

| 脚本文件 | 功能定位 | 关键技术点 |
| :--- | :--- | :--- |
| **`integrate_metadata_all_new.py`** | **总控枢纽** | 串联所有子模块。自动判断输入为单 PRJNA 或列表文件，调度子进程完成全流程，并最终合并所有中间表。 |
| **`parse_bioproject.py`** | **元数据核心解析器** | 调用 `pysradb` 获取 SRA 详细信息；调用 **R 脚本**（`bioproject_extract.R`）通过 `rentrez`/`GEOquery` 抓取 BioProject 摘要、PMID 及期刊信息；调用 **DeepSeek** 解析 ICD-11 疾病大类、样本来源及分组逻辑；输出结构化 Excel。 |
| **`phenotype_generalize(metadata).py`** | **表型字段泛化总结** | 基于白名单（年龄、性别、组织、感染状态等）过滤 SRA 列；利用 DeepSeek 将繁杂的技术字段转化为**中英混合**的语义化表型摘要（如 `age、sex、group(Control/Case)`）。 |
| **`bio_project_info_new.py`** | **项目级信息抽取** | 遍历所有生成的 `*_metadata.xlsx`，提取 `bioproject` 工作表中的期刊名、发表年份、样本量、测序平台等 15 个核心字段，生成管道分隔符文件。 |
| **`metadata_infection_type_new.py`** | **感染类型智能归类** | 基于 ICD-11 码与疾病关键词（如 Mycobacterium -> Bacterial_Intracellular）构建**决策树+正则引擎**，将海量疾病自动归类为 12 类标准感染/宿主响应类型（用于下游模型标签）。 |
| **`parse_metadata_summary_new.py`** | **分组逻辑精炼器** | 解析 `grouping_rules` 工作表，计算每个分组的样本数；再次调用 **DeepSeek** 清理冗余分组维度（如删除实验批次噪音），输出标准化的 `grouping, [labels], [counts]` 三元组。 |

---

## 3. 环境配置与依赖

### 3.1 Python 环境
```bash
conda create -n bio_llm python=3.10
conda activate bio_llm
pip install pysradb pandas openpyxl requests openai
```

### 3.2 R 环境（用于深层 GEO 挖掘）
```R
install.packages(c("GEOquery", "rentrez", "xml2", "jsonlite"))
```

### 3.3 API 密钥配置
```bash
export DEEPSEEK_API_KEY="sk-xxxxx"
# 若使用 Qwen/ChatGPT，修改脚本中的 base_url 与 model 变量
```

---

## 4. 快速执行指南

### 4.1 单数据集处理（调试模式）
```bash
python3 integrate_metadata_all_new.py /path/to/output_dir PRJNA979185
```

### 4.2 批量处理（生产模式）
```bash
# 准备 PRJNA 列表文件（每行一个 ID）
cat PRJNA_list.txt
# PRJNA662344
# PRJNA735200
# ...

# 运行主控脚本
nohup python3 integrate_metadata_all_new.py /data2/boyi/wangkai/metadata_combined PRJNA_list.txt &
```

---

## 5. 输出文件结构说明

最终在输出目录生成以下关键文件，构成完整的表型元数据库：

| 文件名 | 内容描述 |
| :--- | :--- |
| **`combined_metadata_summary.txt`** | **最终汇总表**（管道符分隔）。包含 BioProject、GEO、PMID、期刊、发表年份、疾病大类/小类、ICD-11、感染类型、样本来源、测序平台、样本量、分组标签及对应样本计数。 |
| `PRJNAxxx_metadata.xlsx` | 单个项目明细表。包含 4 个 Sheet：原始 metadata、bioproject 详情、sampletable（含分组映射）、grouping_rules（LLM 生成的分组逻辑）。 |
| `bio_project_info.txt` | 项目级关键信息快照（期刊、DOI、物种等）。 |
| `metadata_infection_type.txt` | 感染类型映射表（用于下游模型标签对齐）。 |
| `grouping_results.txt` | 精炼后的分组结构（如 `"age_group, severity", "[young|old],[mild|severe]", "[30|20],[15|35]"`）。 |

---

## 6. 运行日志示例

```text
>>> Generating PRJNA979185_metadata.xlsx via parse_bioproject ...
[1/4] 获取 BioProject / GEO / PubMed 信息...
✅ PRJNA979185 / GSE228063 / 39160575
[2/4] 获取 pysradb metadata 并清理...
[3/4] 构建 DeepSeek 提示词并调用...
📝 DeepSeek 返回: {"disease_major": "Certain infectious diseases", "disease_minor": "COVID-19", ...}
[4/4] 写出 Excel 文件...
✅ 完成：PRJNA979185_metadata.xlsx
```