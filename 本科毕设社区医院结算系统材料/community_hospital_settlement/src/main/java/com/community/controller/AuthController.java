package com.community.controller;

import com.community.common.Result;
import com.community.dto.LoginDTO;
import com.community.entity.Yisheng;
import com.community.service.AuthService;
import com.community.vo.LoginVO;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 认证接口：登录 / 医生注册
 */
@RestController
@RequestMapping("/api/auth")
public class AuthController {

    private final AuthService authService;

    public AuthController(AuthService authService) {
        this.authService = authService;
    }

    @PostMapping("/login")
    public Result<LoginVO> login(@RequestBody LoginDTO dto) {
        return Result.success("登录成功", authService.login(dto));
    }

    @PostMapping("/register")
    public Result<Void> register(@RequestBody Yisheng yisheng) {
        authService.register(yisheng);
        return Result.success("注册成功", null);
    }
}
