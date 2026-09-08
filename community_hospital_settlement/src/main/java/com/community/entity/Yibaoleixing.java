package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 医保类型表实体（对应论文表9，补充报销比例字段）
 */
@Data
@TableName("yibaoleixing")
public class Yibaoleixing {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String yibaoleixing;

    private Double baoxiaobili;

    private LocalDateTime addtime;
}
