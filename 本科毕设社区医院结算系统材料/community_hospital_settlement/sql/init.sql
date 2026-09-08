-- ============================================================
-- 社区医院结算系统 数据库初始化脚本
-- 数据库名：community_hospital
-- 表结构与字段命名严格对应论文表1~表10（拼音命名）
-- ============================================================

CREATE DATABASE IF NOT EXISTS community_hospital DEFAULT CHARACTER SET utf8mb4;
USE community_hospital;

-- 1. 管理员/用户表
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  username VARCHAR(16) DEFAULT NULL COMMENT '用户名',
  password VARCHAR(16) DEFAULT NULL COMMENT '密码',
  image LONGTEXT COMMENT '头像',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='管理员表';

-- 2. 患者表
DROP TABLE IF EXISTS huanzhe;
CREATE TABLE huanzhe (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  huanzhezhanghao VARCHAR(8) DEFAULT NULL COMMENT '患者账号',
  huanzhexingming VARCHAR(16) DEFAULT NULL COMMENT '患者姓名',
  mima VARCHAR(16) DEFAULT NULL COMMENT '密码',
  xuexing VARCHAR(8) DEFAULT NULL COMMENT '血型',
  xingbie VARCHAR(8) DEFAULT NULL COMMENT '性别',
  nianling INT DEFAULT NULL COMMENT '年龄',
  shouji VARCHAR(16) DEFAULT NULL COMMENT '手机',
  bingfanghao INT DEFAULT NULL COMMENT '病房号',
  chuangweihao INT DEFAULT NULL COMMENT '床位号',
  bingzheng LONGTEXT COMMENT '病症',
  shenfenzheng VARCHAR(32) DEFAULT NULL COMMENT '身份证',
  touxiang LONGTEXT COMMENT '头像',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='患者表';

-- 3. 医生表
DROP TABLE IF EXISTS yisheng;
CREATE TABLE yisheng (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  yishenggonghao VARCHAR(8) DEFAULT NULL COMMENT '医生工号',
  yishengxingming VARCHAR(16) DEFAULT NULL COMMENT '医生姓名',
  mima VARCHAR(16) DEFAULT NULL COMMENT '密码',
  zhicheng VARCHAR(16) DEFAULT NULL COMMENT '职称',
  zhuzhifangxiang VARCHAR(8) DEFAULT NULL COMMENT '主治方向',
  xingbie VARCHAR(8) DEFAULT NULL COMMENT '性别',
  keshi VARCHAR(8) DEFAULT NULL COMMENT '科室',
  lianxidianhua VARCHAR(16) DEFAULT NULL COMMENT '联系电话',
  touxiang LONGTEXT COMMENT '头像',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='医生表';

-- 4. 科室表
DROP TABLE IF EXISTS keshi;
CREATE TABLE keshi (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  keshi VARCHAR(8) DEFAULT NULL COMMENT '科室',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='科室表';

-- 5. 药品信息表
DROP TABLE IF EXISTS yaopinxinxi;
CREATE TABLE yaopinxinxi (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  yaopinmingcheng VARCHAR(32) DEFAULT NULL COMMENT '药品名称',
  tupian LONGTEXT COMMENT '图片',
  yaopinleibie VARCHAR(8) DEFAULT NULL COMMENT '药品类别',
  yongtu LONGTEXT COMMENT '用途',
  guige VARCHAR(32) DEFAULT NULL COMMENT '规格',
  chandi VARCHAR(64) DEFAULT NULL COMMENT '产地',
  yaopinshuliang INT DEFAULT NULL COMMENT '药品数量',
  yaopinshoujia DOUBLE DEFAULT NULL COMMENT '药品售价',
  beizhu LONGTEXT COMMENT '备注',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='药品信息表';

-- 6. 药品费用表（订单）
DROP TABLE IF EXISTS yaopinfeiyong;
CREATE TABLE yaopinfeiyong (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  dingdanbianhao VARCHAR(16) DEFAULT NULL COMMENT '订单编号',
  yishenggonghao VARCHAR(8) DEFAULT NULL COMMENT '医生工号',
  huanzhezhanghao VARCHAR(8) DEFAULT NULL COMMENT '患者账号',
  allyaopinshoujia DOUBLE DEFAULT NULL COMMENT '药费总金额',
  beizhu VARCHAR(256) DEFAULT NULL COMMENT '备注（药品明细）',
  baoxiaofeiyong DOUBLE DEFAULT NULL COMMENT '报销费用',
  shifujine DOUBLE DEFAULT NULL COMMENT '实付金额',
  ispay VARCHAR(8) DEFAULT '未支付' COMMENT '是否支付',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='药品费用表';

-- 7. 医疗服务表
DROP TABLE IF EXISTS yiliaofuwu;
CREATE TABLE yiliaofuwu (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  xiangmumingcheng VARCHAR(32) DEFAULT NULL COMMENT '项目名称',
  xiangmufenlei VARCHAR(8) DEFAULT NULL COMMENT '项目分类',
  xiangmujiage DOUBLE DEFAULT NULL COMMENT '项目价格',
  keyueshijian VARCHAR(64) DEFAULT NULL COMMENT '可约时间',
  xiangmuneirong LONGTEXT COMMENT '项目内容',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='医疗服务表';

-- 8. 医疗费用表（订单）
DROP TABLE IF EXISTS yiliaofeiyong;
CREATE TABLE yiliaofeiyong (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  dingdanbianhao VARCHAR(16) DEFAULT NULL COMMENT '订单编号',
  yishenggonghao VARCHAR(8) DEFAULT NULL COMMENT '医生工号',
  huanzhezhanghao VARCHAR(8) DEFAULT NULL COMMENT '患者账号',
  allxiangmujiage DOUBLE DEFAULT NULL COMMENT '项目总金额',
  beizhu VARCHAR(256) DEFAULT NULL COMMENT '备注（项目明细）',
  baoxiaofeiyong DOUBLE DEFAULT NULL COMMENT '报销费用',
  shifufeiyong DOUBLE DEFAULT NULL COMMENT '实付费用',
  ispay VARCHAR(8) DEFAULT '未支付' COMMENT '是否支付',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='医疗费用表';

-- 9. 医保类型表（补充 baoxiaobili 报销比例字段，用于报销扣减逻辑）
DROP TABLE IF EXISTS yibaoleixing;
CREATE TABLE yibaoleixing (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  yibaoleixing VARCHAR(32) DEFAULT NULL COMMENT '医保类型',
  baoxiaobili DOUBLE DEFAULT NULL COMMENT '报销比例，如0.8表示80%',
  addtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='医保类型表';

-- 10. 配置文件表
DROP TABLE IF EXISTS config;
CREATE TABLE config (
  id BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键',
  name VARCHAR(256) DEFAULT NULL COMMENT '配置参数名称',
  value VARCHAR(128) DEFAULT NULL COMMENT '配置参数值',
  url VARCHAR(512) DEFAULT NULL COMMENT 'url',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='配置文件表';

-- ============================================================
-- 初始化基础数据
-- ============================================================

-- 管理员账号（admin / 123456）
INSERT INTO users (username, password) VALUES ('admin', '123456');

-- 科室
INSERT INTO keshi (keshi) VALUES ('内科'), ('外科'), ('妇产科'), ('儿科');

-- 医保类型（报销比例）
INSERT INTO yibaoleixing (yibaoleixing, baoxiaobili) VALUES
('城镇职工基本医疗保险', 0.80),
('城乡居民基本医疗保险', 0.70),
('大病保险', 0.90);

-- 医生（工号 / 姓名 / 密码 / 职称 / 主治方向 / 性别 / 科室 / 电话）
INSERT INTO yisheng (yishenggonghao, yishengxingming, mima, zhicheng, zhuzhifangxiang, xingbie, keshi, lianxidianhua) VALUES
('P001', '王凯', '001', '主治医师', '内科', '男', '内科', '13800138001'),
('P002', '秦颖', '002', '副主任医师', '外科', '女', '外科', '13800138002');

-- 患者（账号 / 姓名 / 密码 / 血型 / 性别 / 年龄 / 手机 / 病房号 / 床位号 / 身份证）
INSERT INTO huanzhe (huanzhezhanghao, huanzhexingming, mima, xuexing, xingbie, nianling, shouji, bingfanghao, chuangweihao, shenfenzheng) VALUES
('P001', '徐雨', '001', 'A', '女', 28, '13800138003', 101, 1, '320100199601010011'),
('P002', '许灵莹', '002', 'AB', '女', 35, '13800138004', 102, 2, '320100198901010022');

-- 药品信息（名称 / 类别 / 用途 / 规格 / 产地 / 数量 / 售价）
INSERT INTO yaopinxinxi (yaopinmingcheng, yaopinleibie, yongtu, guige, chandi, yaopinshuliang, yaopinshoujia) VALUES
('蒙脱石散', '内服', '止泻', '3g*10袋', '江苏', 100, 12.50),
('布洛芬缓释胶囊', '内服', '解热镇痛', '0.3g*20粒', '北京', 200, 20.80),
('感康', '内服', '感冒用药', '12片/盒', '吉林', 150, 15.00),
('硫磺软膏', '外用', '皮肤病', '20g/瓶', '上海', 80, 8.00);

-- 医疗服务（项目名称 / 分类 / 价格 / 可约时间 / 内容）
INSERT INTO yiliaofuwu (xiangmumingcheng, xiangmufenlei, xiangmujiage, keyueshijian, xiangmuneirong) VALUES
('内科检查', '检查', 30.00, '周一至周五 8:00-17:00', '常规内科检查'),
('B超检查', '检查', 120.00, '周一至周五 8:00-17:00', '腹部B超'),
('CT检查', '检查', 300.00, '需预约', 'CT影像检查'),
('血常规', '化验', 25.00, '周一至周日 8:00-17:00', '血常规化验');
