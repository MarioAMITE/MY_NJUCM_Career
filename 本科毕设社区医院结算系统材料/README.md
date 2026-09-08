# 社区医院结算系统

## 这个系统是干什么的

社区医院里，患者看完病要结账，医生要给患者开药、开检查。

- 医生或管理员给患者勾选药品、医疗服务，系统自动算出总费用；
- 选一个医保类型，按报销比例算出报销金额，剩下的就是患者要实付的钱；
- 患者自己登录，看到自己的费用单，点支付就完成缴费；
- 费用可以导出成 Excel，也可以打印。

## 毕设当时的设计

毕设阶段用的技术是 **Eclipse + Spring Boot + MySQL + Java**，B/S 模式，前后端没分开，页面跟着 Spring Boot 一起渲染。

**三种角色**，权限各不相同：

| 角色 | 能做什么 |
|---|---|
| 管理员 | 管所有信息：医生、患者、科室、药品、医疗服务、医保类型，也能下单、改单 |
| 医生 | 管患者信息、下单结算，但只能看到自己经手的患者和费用 |
| 患者 | 只能看自己的费用单，然后支付，改改自己的资料 |

**十张数据表**，表名和字段名都是拼音（论文里就是这么定的）：`users`（管理员）、`huanzhe`（患者）、`yisheng`（医生）、`keshi`（科室）、`yaopinxinxi`（药品信息）、`yaopinfeiyong`（药品费用）、`yiliaofuwu`（医疗服务）、`yiliaofeiyong`（医疗费用）、`yibaoleixing`（医保类型）、`config`（配置）。

**核心业务**就是两张费用单：

1. 药品费用：勾选药品（带数量）→ 总金额 = 售价 × 数量之和 → 选医保类型 → 报销 = 总金额 × 报销比例 → 实付 = 总金额 − 报销；
2. 医疗费用：勾选医疗服务 → 总金额 = 各项目价格之和 → 同样的报销逻辑。

关于注册，论文里有个约束：**只有医生能注册**。管理员是数据库里初始化好的，不在页面上开放注册；患者也不用注册，由医生建档后直接登录缴费。

## 这次用 Claude Code 改了哪些地方

老版本在新电脑上跑不起来，而且代码是刚学的时候写的，比较乱。于是用 Claude Code 把整个项目重新捋了一遍，主要动了这几块：

1. **前端重写成 Vue3**。毕设时是服务端渲染的页面，这次换成了 Vue3 + Element Plus 的前后端分离写法，列表、表单、弹窗这些交互比原来顺手。
2. **后端升级到 Spring Boot 3.4**。跑不起来了，所以升到了 3.4。
3. **登录改成 JWT**。原来是 session，改成 JWT 后前后端分离更干净，前端存 token，每次请求带上。
4. **数据访问换成 MyBatis-Plus**。原来手写的 SQL 和 JDBC 拼装比较多，现在用 MyBatis-Plus 的 BaseMapper 和 LambdaQueryWrapper，增删改查快很多。
5. **补了报销比例字段**。论文里医保类型表没单独列「报销比例」这一列，但正文里「选医保类型扣报销」要用到它，所以我在 `yibaoleixing` 表里加了 `baoxiaobili`，下单时按这个比例算报销。
6. **导出用 EasyExcel**，打印用浏览器的打印功能（`window.print()`）。

## 使用说明

### 1. 初始化数据库

本地要有 MySQL 8。把 `community_hospital_settlement/sql/init.sql` 导进去：

```
mysql -u root -p123456 --default-character-set=utf8mb4 < sql/init.sql
```

默认连的是 `localhost:3306`，库名 `community_hospital`，账号 `root` / `123456`。跟环境对不上就改 `src/main/resources/application.yml`。

### 2. 启动后端

在 `community_hospital_settlement/` 目录下：

```
mvn spring-boot:run
```

或者打包成 jar 再跑：

```
mvn clean package -DskipTests
java -jar target/community-hospital-settlement-0.0.1-SNAPSHOT.jar
```

后端起来后监听 8080 端口。

### 3. 启动前端

```
cd community_hospital_settlement/frontend
npm install
npm run dev
```

前端默认开在 5173 端口，`/api` 的请求会自动代理到后端的 8080。

## 怎么登录使用

后端和前端都起来之后，浏览器打开 **http://localhost:5173**，就会到登录页。

登录需要三样东西都填对：**用户名、密码、角色**。角色在下拉里选「管理员 / 医生 / 患者」。

系统里预置了这几个账号，可以直接拿来试：

| 角色 | 用户名 | 密码 |
|---|---|---|
| 管理员 | admin | 123456 |
| 医生 | P001（王凯） | 001 |
| 医生 | P002（秦颖） | 002 |
| 患者 | P001（徐雨） | 001 |
| 患者 | P002（许灵莹） | 002 |

使用流程：

1. 用 **admin / 123456**（管理员）登录，先把基础数据备好：科室、药品、医疗服务、医保类型，再到「患者信息」里建两个患者账号；
2. 退出，用 **P001 / 001**（医生王凯）登录，进「药品费用」点「下单」，选患者、勾药品、填数量、选医保类型，右边会实时显示总金额、报销、实付，确认下单；
3. 再退出，用患者 **P001 / 001**（徐雨）登录，进「药品费用」能看到刚才那张单子，状态是「未支付」，点「支付」就变成「已支付」；
4. 费用页右上角还有「导出」（下载 Excel）和「打印」。

如果是新来的医生，在登录页点「注册」，填工号、姓名、职称、科室、电话就能自助注册，注册完直接登录。工号重复、电话格式不对都会被拦下来。

## 目录结构

```
community_hospital_settlement/
├── pom.xml                    后端 Maven 配置
├── sql/init.sql               建表 + 示例数据
├── src/main/java/com/community/   后端代码
│   ├── entity/                10 个实体（拼音字段）
│   ├── mapper/                MyBatis-Plus 接口
│   ├── service/               登录、下单结算逻辑
│   ├── controller/            认证 / 公共 / 管理员 / 医生 / 患者 / 导出
│   ├── security/              JWT + 登录拦截器
│   └── common/                统一返回、异常处理
├── src/main/resources/application.yml
└── frontend/                  Vue3 前端
    └── src/
        ├── views/             登录、各业务页面
        ├── router/            路由 + 登录/角色守卫
        ├── store/             用户状态（token、角色）
        └── utils/request.js   axios 封装
```

## 几点说明

- 表名、字段名用的是拼音，主要是懒得改了，所以就保留原本毕业设计的设计。
- 费用单里「勾了哪些药品/服务」存成文字串放在 `beizhu` 字段里（比如「布洛芬缓释胶囊×2, 感康×1」），金额字段存的是汇总值，这样不用多建表。
- 前端界面是医疗蓝色的后台风格。
