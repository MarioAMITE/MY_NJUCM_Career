package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * 配置文件表实体（对应论文表10）
 */
@Data
@TableName("config")
public class Config {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String name;

    private String value;

    private String url;
}
