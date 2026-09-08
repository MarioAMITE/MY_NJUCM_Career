package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 科室表实体（对应论文表4）
 */
@Data
@TableName("keshi")
public class Keshi {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String keshi;

    private LocalDateTime addtime;
}
