package com.community.dto;

import lombok.Data;

import java.util.List;

/**
 * 创建医疗费用订单参数
 */
@Data
public class MedicalFeeCreateDTO {

    /** 患者账号 */
    private String huanzhezhanghao;

    /** 医保类型ID（可选，用于报销扣减） */
    private Long yibaoleixingId;

    /** 勾选的医疗服务ID */
    private List<Long> itemIds;
}
