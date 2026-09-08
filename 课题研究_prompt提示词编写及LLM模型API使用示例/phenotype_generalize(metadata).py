#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
融合 pysradb + DeepSeek，总结 PRJNA 样本表型信息
- 自动下载 metadata
- 列举每个字段及其取值
- 使用重点字段白名单控制单一值列
- 交给 DeepSeek 生成中英混合总结
"""

import os
import csv
import time
import pandas as pd
from openai import OpenAI

# ============== 配置部分 ==============
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
PRJNA_LIST_FILE = r"/mnt/nfs/PublishedGEO/infectiondisease_wangkai/code/phenotype/PRJNA.txt"
OUTPUT_CSV = r"/mnt/nfs/PublishedGEO/infectiondisease_wangkai/code/phenotype/phenotype_summary.csv"

# 重点字段白名单（即便只有单一值也保留）
KEY_FIELDS = [
    "age", "age_years", "age_weeks",
    "sex", "gender",
    "race", "ethnicity",
    "tissue", "cell_type",
    "disease", "disease_state", "health_status",
    "infection", "infection_status",
    "vaccine", "vaccination",
    "timepoint", "visit", "visit_id",
    "collection_location", "geo_loc_name",
    "treatment", "group", "case"
]

# ============== DeepSeek 提示词 ==============
SYSTEM_PROMPT = f"""
你是一个专业的生物信息学数据分析助手。
我会提供 NCBI SRA metadata 的字段及其取值。
你的任务是：
1. 识别其中与样本本身有关的表型字段（如 age, sex, disease, tissue, infection, vaccination, timepoint 等）。
2. 忽略技术性字段（如 run_accession, file size, sequencing_platform, library_layout 等）。
3. 将输出总结为中英混合形式，中文解释简洁明了。
4. 对每个变量，如果有分组值，请列出英文取值并附中文含义。
5. 特别注意以下重点字段，如出现务必保留：
{", ".join(KEY_FIELDS)}

输出格式要求：
- 每行以 “PRJNA编号,” 开头。
- 变量名保留英文，但每个变量后添加简短中文注释。
- 若有分类变量或取值，请列出英文值并附中文含义。
- 严格模仿以下格式：

示例输出：
PRJNA735200,age_weeks、sex、case（case、control、neither）、既往感染史（malaria_before_m3_5）、感染状态（malaria_status）、地区传播强度或类型（malaria_transmission）、从观察起点到首次疟疾感染的时间（time_to_malaria）、刺激（stimulation）、疫苗接种分组（vaccine）、采样时间点（visit）
PRJNA815324,age、sex、race、种族分类（ethnicity）、group（前中后期Pre、Mid、Post、对照Control、暴露Exposed、产生免疫应答Immune +、Immune）、SARS-CoV-2 PCR结果（pcr_test_for_sars-cov-2）
PRJNA400331,age、sex、race、cell_type(Tcells)、group（对照Control、病例case、感染者中未发展为疾病的人Not a PP case）、既往结核病诊断（previousdiagnosisoftb）、qtf结果、刺激（stimulation）、tst结果
PRJNA891054,sex、covid-19_positive（positive、negative）、距离第一次采样天数（days_since_first_sample）、受试者在第一次采样时的临床或免疫学分类（patient_classification_at_first_sample，SARS-CoV-2_Unknown_Ab_Negative、SARS-CoV-2_Positive_Ab_Positive...）、第几次采样（sampling_time_point_label，T1、T2、T4、T8...）
PRJNA873691,页面未提供原始数据
PRJNA401870,gender、种族分类（ethnicity）、Protection（NOT PROTECTED、PROTECTED、NA）、treatment（Ad35.CS+RTSS+RTSS、RTSS+RTSS+RTSS、NA）
PRJNA768419,age、sex、disease_state（sepsis、healthy）收集地区collection_location、collection_site（ICU、Emergency Room）、in_hospital_mortality（Survived、Died）、SOFA评分
PRJNA753724,cell_type(Blood Monocytes、Blood B cells)、是否感染hiv-1_acquisition、timepoint（pre-vaccination、month 7、month 12）、采样标示visit_id
"""

# ============== 工具函数 ==============

def init_deepseek_client(api_key):
    return OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def read_prjna_list(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_metadata_with_pysradb(prj_id):
    """用 pysradb 直接获取 metadata"""
    try:
        import pysradb
        db = pysradb.SRAweb()
        df = db.metadata(prj_id, detailed=True)
        if df is None or df.empty:
            print(f" {prj_id} metadata 为空")
            return None
        return df
    except Exception as e:
        print(f"无法通过 pysradb 获取 {prj_id} metadata: {e}")
        return None


def summarize_metadata_for_ai(df):
    """格式化 metadata，保留重点字段 + 分组字段"""
    if df is None or df.empty:
        return ""

    summary_lines = []
    for col in df.columns:
        unique_vals = df[col].dropna().astype(str).unique().tolist()
        # 只展示前10个值
        preview = ", ".join(unique_vals[:10])

        # 过滤逻辑：
        # 1. 如果列只有一个唯一值，但列名在白名单中 → 保留
        # 2. 如果列有多个唯一值 → 保留
        # 3. 其他情况 → 跳过
        if len(unique_vals) == 1 and col.lower() not in KEY_FIELDS:
            continue
        if not preview.strip():
            continue

        summary_lines.append(f"[{col}] → {preview}")

    return "\n".join(summary_lines)

def analyze_with_deepseek(client, prjna_id, text):
    if not text.strip():
        return f"{prjna_id},页面未提供原始数据"
    prompt = f"以下是 {prjna_id} 的 SRA metadata 字段及取值，请总结表型信息：\n{text[:8000]}"
    try:
        resp = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=800
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"? DeepSeek 分析失败 {prjna_id}: {e}")
        return f"{prjna_id},分析失败"

# ============== 主程序 ==============

def main():
    client = init_deepseek_client(DEEPSEEK_API_KEY)
    prjna_list = read_prjna_list(PRJNA_LIST_FILE)
    results = []

    for prjna_id in prjna_list:
        print(f"\n?? 正在处理 {prjna_id} ...")
        df = get_metadata_with_pysradb(prjna_id)
        if df is None or df.empty:
            results.append([prjna_id, f"{prjna_id},页面未提供原始数据"])
            continue

        text_summary = summarize_metadata_for_ai(df)
        if not text_summary.strip():
            results.append([prjna_id, f"{prjna_id},页面未提供原始数据"])
            continue

        summary = analyze_with_deepseek(client, prjna_id, text_summary)
        print(f"  ? 结果: {summary}")
        results.append([prjna_id, summary])

        time.sleep(2)  # 防止API限流

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["PRJNA编号", "表型信息总结"])
        writer.writerows(results)

    print(f"\n 所有 PRJNA 处理完成，结果已保存到：{OUTPUT_CSV}")

if __name__ == "__main__":
    main()
