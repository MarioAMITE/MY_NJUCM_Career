package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 医生表实体（对应论文表3）
 */
@Data
@TableName("yisheng")
public class Yisheng {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String yishenggonghao;

    private String yishengxingming;

    private String mima;

    private String zhicheng;

    private String zhuzhifangxiang;

    private String xingbie;

    private String keshi;

    private String lianxidianhua;

    private String touxiang;

    private LocalDateTime addtime;
}
