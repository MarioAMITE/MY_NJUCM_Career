package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 药品信息表实体（对应论文表5）
 */
@Data
@TableName("yaopinxinxi")
public class Yaopinxinxi {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String yaopinmingcheng;

    private String tupian;

    private String yaopinleibie;

    private String yongtu;

    private String guige;

    private String chandi;

    private Integer yaopinshuliang;

    private Double yaopinshoujia;

    private String beizhu;

    private LocalDateTime addtime;
}
