package com.community.vo;

import lombok.Data;

/**
 * 登录返回结果
 */
@Data
public class LoginVO {

    private String token;

    private Long id;

    private String username;

    private String role;

    /** 显示名称（姓名 / 用户名） */
    private String realName;
}
