package com.community.dto;

import lombok.Data;

import java.util.List;

/**
 * 创建药品费用订单参数
 */
@Data
public class DrugFeeCreateDTO {

    /** 患者账号 */
    private String huanzhezhanghao;

    /** 医保类型ID（可选，用于报销扣减） */
    private Long yibaoleixingId;

    /** 勾选的药品及其数量 */
    private List<Item> items;

    @Data
    public static class Item {
        private Long yaopinId;
        private Integer shuliang;
    }
}
