package com.community.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

/**
 * 管理员/用户表实体（对应论文表1）
 */
@Data
@TableName("users")
public class Users {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String username;

    private String password;

    private String image;

    private LocalDateTime addtime;
}
