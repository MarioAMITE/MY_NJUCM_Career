package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 医疗费用表实体（订单，对应论文表8）
 */
@Data
@TableName("yiliaofeiyong")
public class Yiliaofeiyong {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String dingdanbianhao;

    private String yishenggonghao;

    private String huanzhezhanghao;

    private Double allxiangmujiage;

    private String beizhu;

    private Double baoxiaofeiyong;

    private Double shifufeiyong;

    private String ispay;

    private LocalDateTime addtime;
}
