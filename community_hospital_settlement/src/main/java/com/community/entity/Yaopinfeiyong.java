package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 药品费用表实体（订单，对应论文表6）
 */
@Data
@TableName("yaopinfeiyong")
public class Yaopinfeiyong {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String dingdanbianhao;

    private String yishenggonghao;

    private String huanzhezhanghao;

    private Double allyaopinshoujia;

    private String beizhu;

    private Double baoxiaofeiyong;

    private Double shifujine;

    private String ispay;

    private LocalDateTime addtime;
}
