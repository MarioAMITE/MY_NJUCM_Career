package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 患者表实体（对应论文表2）
 */
@Data
@TableName("huanzhe")
public class Huanzhe {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String huanzhezhanghao;

    private String huanzhexingming;

    private String mima;

    private String xuexing;

    private String xingbie;

    private Integer nianling;

    private String shouji;

    private Integer bingfanghao;

    private Integer chuangweihao;

    private String bingzheng;

    private String shenfenzheng;

    private String touxiang;

    private LocalDateTime addtime;
}
