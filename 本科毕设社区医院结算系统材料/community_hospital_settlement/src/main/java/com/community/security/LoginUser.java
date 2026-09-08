package com.community.security;

import lombok.Data;

/**
 * 当前登录用户信息
 */
@Data
public class LoginUser {

    private Long id;

    /** 登录账号（管理员用户名 / 医生工号 / 患者账号） */
    private String username;

    /** 角色：ADMIN / DOCTOR / PATIENT */
    private String role;
}
