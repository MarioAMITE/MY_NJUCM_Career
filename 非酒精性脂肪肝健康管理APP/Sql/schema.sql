-- ============================================================
-- 非酒精性脂肪肝健康管理APP 数据库结构（MySQL 5.7+ / 8.0）
-- 字符集 utf8mb4
-- 说明：患者档案覆盖生化指标、体格指标等 20 余项特征。
-- ============================================================

CREATE DATABASE IF NOT EXISTS nafld_health
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_general_ci;

USE nafld_health;

-- ------------------------------------------------------------
-- 用户表（患者 / 医生 / 管理员）
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `user` (
  user_id       INT AUTO_INCREMENT PRIMARY KEY,
  username      VARCHAR(50)  NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role          VARCHAR(20)  NOT NULL DEFAULT 'patient' COMMENT 'patient/doctor/admin',
  real_name     VARCHAR(50),
  phone         VARCHAR(20),
  created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户';

-- ------------------------------------------------------------
-- 患者电子档案（20+ 特征）
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS patient_profile (
  profile_id          INT AUTO_INCREMENT PRIMARY KEY,
  user_id             INT NOT NULL,
  real_name           VARCHAR(50),
  gender              VARCHAR(10),
  birth_date          DATE,
  height              DECIMAL(5,2) COMMENT '身高cm',
  weight              DECIMAL(5,2) COMMENT '体重kg',
  bmi                 DECIMAL(5,2) COMMENT '体质指数',
  waistline           DECIMAL(5,2) COMMENT '腰围cm',
  alt                 DECIMAL(8,2) COMMENT '谷丙转氨酶ALT(U/L)',
  ast                 DECIMAL(8,2) COMMENT '谷草转氨酶AST(U/L)',
  ggt                 DECIMAL(8,2) COMMENT 'γ-谷氨酰转肽酶GGT(U/L)',
  total_cholesterol   DECIMAL(8,2) COMMENT '总胆固醇TC(mmol/L)',
  triglyceride        DECIMAL(8,2) COMMENT '甘油三酯TG(mmol/L)',
  hdl                 DECIMAL(8,2) COMMENT '高密度脂蛋白HDL(mmol/L)',
  ldl                 DECIMAL(8,2) COMMENT '低密度脂蛋白LDL(mmol/L)',
  fasting_glucose     DECIMAL(8,2) COMMENT '空腹血糖FBG(mmol/L)',
  uric_acid           DECIMAL(8,2) COMMENT '尿酸UA(μmol/L)',
  hba1c               DECIMAL(5,2) COMMENT '糖化血红蛋白HbA1c(%)',
  liver_fat_content   DECIMAL(5,2) COMMENT '肝脂肪含量(%)',
  bp_systolic         INT COMMENT '收缩压(mmHg)',
  bp_diastolic        INT COMMENT '舒张压(mmHg)',
  fibrosis_stage      VARCHAR(10) COMMENT '肝纤维化分期F0-F4',
  diagnosis_date      DATE,
  note                VARCHAR(500),
  CONSTRAINT fk_profile_user FOREIGN KEY (user_id) REFERENCES `user`(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='患者电子档案';

-- ------------------------------------------------------------
-- 行为日志（饮食/运动/用药/睡眠/体重）
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS behavior_log (
  log_id               BIGINT AUTO_INCREMENT PRIMARY KEY,
  profile_id           INT NOT NULL,
  log_date             DATETIME NOT NULL,
  log_type             VARCHAR(20) NOT NULL COMMENT 'diet/exercise/medication/sleep/weight',
  content              VARCHAR(500),
  calories             DECIMAL(8,2) COMMENT '热量kcal',
  steps                INT COMMENT '步数',
  duration_minutes     INT COMMENT '时长(分钟)',
  medication_adherence VARCHAR(20) COMMENT '用药依从性',
  remark               VARCHAR(500),
  CONSTRAINT fk_log_profile FOREIGN KEY (profile_id) REFERENCES patient_profile(profile_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='行为日志';

-- ------------------------------------------------------------
-- 商品
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS product (
  product_id  INT AUTO_INCREMENT PRIMARY KEY,
  name        VARCHAR(100) NOT NULL,
  category    VARCHAR(50),
  price       DECIMAL(10,2),
  stock       INT DEFAULT 0,
  description VARCHAR(500),
  image_url   VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='商品';

-- ------------------------------------------------------------
-- 订单 / 订单明细
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS orders (
  order_id     INT AUTO_INCREMENT PRIMARY KEY,
  user_id      INT NOT NULL,
  order_date   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total_amount DECIMAL(10,2),
  status       VARCHAR(20) DEFAULT 'pending',
  CONSTRAINT fk_order_user FOREIGN KEY (user_id) REFERENCES `user`(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单';

CREATE TABLE IF NOT EXISTS order_item (
  order_item_id INT AUTO_INCREMENT PRIMARY KEY,
  order_id      INT NOT NULL,
  product_id    INT NOT NULL,
  quantity      INT NOT NULL DEFAULT 1,
  unit_price    DECIMAL(10,2),
  CONSTRAINT fk_item_order   FOREIGN KEY (order_id)   REFERENCES orders(order_id),
  CONSTRAINT fk_item_product FOREIGN KEY (product_id) REFERENCES product(product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单明细';

-- ------------------------------------------------------------
-- 论坛帖子 / 回帖
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS post (
  post_id    INT AUTO_INCREMENT PRIMARY KEY,
  user_id    INT NOT NULL,
  board      VARCHAR(50) COMMENT '板块',
  title      VARCHAR(200) NOT NULL,
  content    TEXT,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_post_user FOREIGN KEY (user_id) REFERENCES `user`(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='帖子';

CREATE TABLE IF NOT EXISTS reply (
  reply_id   INT AUTO_INCREMENT PRIMARY KEY,
  post_id    INT NOT NULL,
  user_id    INT NOT NULL,
  content    TEXT,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_reply_post FOREIGN KEY (post_id) REFERENCES post(post_id),
  CONSTRAINT fk_reply_user FOREIGN KEY (user_id) REFERENCES `user`(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='回帖';

-- ------------------------------------------------------------
-- 医患咨询消息
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS consult_message (
  message_id  BIGINT AUTO_INCREMENT PRIMARY KEY,
  session_id  INT NOT NULL,
  sender_id   INT NOT NULL,
  receiver_id INT NOT NULL,
  content     TEXT,
  sent_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  is_read     TINYINT(1) DEFAULT 0,
  CONSTRAINT fk_msg_sender   FOREIGN KEY (sender_id)   REFERENCES `user`(user_id),
  CONSTRAINT fk_msg_receiver FOREIGN KEY (receiver_id) REFERENCES `user`(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='医患咨询消息';

-- ------------------------------------------------------------
-- 智能饮食分析记录
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ai_analysis_record (
  record_id   BIGINT AUTO_INCREMENT PRIMARY KEY,
  profile_id  INT NOT NULL,
  input       VARCHAR(500) COMMENT '饮食描述或图片路径',
  result      TEXT,
  analyzed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_ai_profile FOREIGN KEY (profile_id) REFERENCES patient_profile(profile_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='饮食分析记录';
