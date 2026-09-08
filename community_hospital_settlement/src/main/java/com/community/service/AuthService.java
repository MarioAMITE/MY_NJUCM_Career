package com.community.service;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.dto.LoginDTO;
import com.community.entity.Huanzhe;
import com.community.entity.Users;
import com.community.entity.Yisheng;
import com.community.mapper.HuanzheMapper;
import com.community.mapper.UsersMapper;
import com.community.mapper.YishengMapper;
import com.community.security.JwtUtil;
import com.community.vo.LoginVO;
import org.springframework.stereotype.Service;

/**
 * 认证服务：登录 / 医生注册
 */
@Service
public class AuthService {

    private final UsersMapper usersMapper;
    private final YishengMapper yishengMapper;
    private final HuanzheMapper huanzheMapper;
    private final JwtUtil jwtUtil;

    public AuthService(UsersMapper usersMapper, YishengMapper yishengMapper,
                       HuanzheMapper huanzheMapper, JwtUtil jwtUtil) {
        this.usersMapper = usersMapper;
        this.yishengMapper = yishengMapper;
        this.huanzheMapper = huanzheMapper;
        this.jwtUtil = jwtUtil;
    }

    /**
     * 登录：用户名 + 密码 + 角色
     */
    public LoginVO login(LoginDTO dto) {
        String role = dto.getRole();
        if ("ADMIN".equals(role)) {
            Users u = usersMapper.selectOne(new LambdaQueryWrapper<Users>()
                    .eq(Users::getUsername, dto.getUsername()));
            if (u == null || !u.getPassword().equals(dto.getPassword())) {
                throw new BusinessException("账号或密码不正确");
            }
            return buildVO(u.getId(), u.getUsername(), "ADMIN", u.getUsername());
        } else if ("DOCTOR".equals(role)) {
            Yisheng y = yishengMapper.selectOne(new LambdaQueryWrapper<Yisheng>()
                    .eq(Yisheng::getYishenggonghao, dto.getUsername()));
            if (y == null || !y.getMima().equals(dto.getPassword())) {
                throw new BusinessException("账号或密码不正确");
            }
            return buildVO(y.getId(), y.getYishenggonghao(), "DOCTOR", y.getYishengxingming());
        } else if ("PATIENT".equals(role)) {
            Huanzhe h = huanzheMapper.selectOne(new LambdaQueryWrapper<Huanzhe>()
                    .eq(Huanzhe::getHuanzhezhanghao, dto.getUsername()));
            if (h == null || !h.getMima().equals(dto.getPassword())) {
                throw new BusinessException("账号或密码不正确");
            }
            return buildVO(h.getId(), h.getHuanzhezhanghao(), "PATIENT", h.getHuanzhexingming());
        } else {
            throw new BusinessException("角色不正确");
        }
    }

    /**
     * 医生注册（校验工号唯一、联系电话格式）
     */
    public void register(Yisheng yisheng) {
        Long count = yishengMapper.selectCount(new LambdaQueryWrapper<Yisheng>()
                .eq(Yisheng::getYishenggonghao, yisheng.getYishenggonghao()));
        if (count != null && count > 0) {
            throw new BusinessException("该医生工号已注册");
        }
        if (yisheng.getLianxidianhua() == null || !yisheng.getLianxidianhua().matches("\\d{11}")) {
            throw new BusinessException("联系电话格式不正确，需为11位数字");
        }
        yishengMapper.insert(yisheng);
    }

    private LoginVO buildVO(Long id, String username, String role, String realName) {
        LoginVO vo = new LoginVO();
        vo.setToken(jwtUtil.generateToken(id, username, role));
        vo.setId(id);
        vo.setUsername(username);
        vo.setRole(role);
        vo.setRealName(realName);
        return vo;
    }
}
