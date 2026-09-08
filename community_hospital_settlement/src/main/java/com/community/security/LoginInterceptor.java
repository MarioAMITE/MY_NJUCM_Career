package com.community.security;

import com.community.common.Result;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.jsonwebtoken.Claims;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

/**
 * 登录认证与角色权限拦截器
 */
@Component
public class LoginInterceptor implements HandlerInterceptor {

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // CORS 预检请求直接放行
        if ("OPTIONS".equalsIgnoreCase(request.getMethod())) {
            return true;
        }

        String uri = request.getRequestURI();

        // 放行公共接口
        if (isPublic(uri)) {
            return true;
        }

        // 校验 token
        String auth = request.getHeader("Authorization");
        if (auth == null || !auth.startsWith("Bearer ")) {
            return reject(response, 401, "未登录或登录已失效");
        }
        Claims claims = jwtUtil.parseToken(auth.substring(7));
        if (claims == null) {
            return reject(response, 401, "未登录或登录已失效");
        }

        LoginUser user = new LoginUser();
        user.setId(claims.get("id", Long.class));
        user.setUsername(claims.getSubject());
        user.setRole(claims.get("role", String.class));
        UserContext.set(user);

        // 角色权限校验
        String required = requiredRole(uri);
        if (required != null && !required.equals(user.getRole())) {
            return reject(response, 403, "权限不足");
        }
        return true;
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) {
        UserContext.clear();
    }

    private boolean isPublic(String uri) {
        return uri.startsWith("/api/auth/")
                || uri.equals("/api/common/keshi")
                || uri.equals("/api/common/yibaoleixing");
    }

    private String requiredRole(String uri) {
        if (uri.startsWith("/api/admin/")) {
            return "ADMIN";
        } else if (uri.startsWith("/api/doctor/")) {
            return "DOCTOR";
        } else if (uri.startsWith("/api/patient/")) {
            return "PATIENT";
        }
        // /api/common/** 与 /api/export/** 允许所有已登录用户
        return null;
    }

    private boolean reject(HttpServletResponse response, int code, String message) throws Exception {
        response.setStatus(code);
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().write(MAPPER.writeValueAsString(Result.error(code, message)));
        return false;
    }

    private final JwtUtil jwtUtil;

    public LoginInterceptor(JwtUtil jwtUtil) {
        this.jwtUtil = jwtUtil;
    }
}
