package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 医疗服务表实体（对应论文表7）
 */
@Data
@TableName("yiliaofuwu")
public class Yiliaofuwu {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String xiangmumingcheng;

    private String xiangmufenlei;

    private Double xiangmujiage;

    private String keyueshijian;

    private String xiangmuneirong;

    private LocalDateTime addtime;
}
