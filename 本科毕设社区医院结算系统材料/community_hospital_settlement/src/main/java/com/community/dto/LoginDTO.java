package com.community.dto;

import lombok.Data;

/**
 * 登录请求参数
 */
@Data
public class LoginDTO {

    private String username;

    private String password;

    /** 角色：ADMIN / DOCTOR / PATIENT */
    private String role;
}
