package com.community.controller;

import com.community.common.BusinessException;
import com.community.common.Result;
import com.community.entity.Huanzhe;
import com.community.entity.Keshi;
import com.community.entity.Users;
import com.community.entity.Yibaoleixing;
import com.community.entity.Yisheng;
import com.community.mapper.HuanzheMapper;
import com.community.mapper.KeshiMapper;
import com.community.mapper.UsersMapper;
import com.community.mapper.YibaoleixingMapper;
import com.community.mapper.YishengMapper;
import com.community.security.LoginUser;
import com.community.security.UserContext;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

/**
 * 公共接口：个人资料、修改密码、科室/医保类型下拉数据
 */
@RestController
@RequestMapping("/api/common")
public class CommonController {

    private final UsersMapper usersMapper;
    private final YishengMapper yishengMapper;
    private final HuanzheMapper huanzheMapper;
    private final KeshiMapper keshiMapper;
    private final YibaoleixingMapper yibaoleixingMapper;

    public CommonController(UsersMapper usersMapper, YishengMapper yishengMapper,
                            HuanzheMapper huanzheMapper, KeshiMapper keshiMapper,
                            YibaoleixingMapper yibaoleixingMapper) {
        this.usersMapper = usersMapper;
        this.yishengMapper = yishengMapper;
        this.huanzheMapper = huanzheMapper;
        this.keshiMapper = keshiMapper;
        this.yibaoleixingMapper = yibaoleixingMapper;
    }

    /** 当前登录用户信息 */
    @GetMapping("/profile")
    public Result<Object> profile() {
        LoginUser user = UserContext.get();
        if ("ADMIN".equals(user.getRole())) {
            return Result.success(usersMapper.selectById(user.getId()));
        } else if ("DOCTOR".equals(user.getRole())) {
            return Result.success(yishengMapper.selectById(user.getId()));
        } else {
            return Result.success(huanzheMapper.selectById(user.getId()));
        }
    }

    /** 修改密码 */
    @PutMapping("/password")
    public Result<Void> password(@RequestBody Map<String, String> body) {
        String oldPassword = body.get("oldPassword");
        String newPassword = body.get("newPassword");
        LoginUser user = UserContext.get();

        if ("ADMIN".equals(user.getRole())) {
            Users u = usersMapper.selectById(user.getId());
            checkPassword(u.getPassword(), oldPassword, newPassword);
            u.setPassword(newPassword);
            usersMapper.updateById(u);
        } else if ("DOCTOR".equals(user.getRole())) {
            Yisheng y = yishengMapper.selectById(user.getId());
            checkPassword(y.getMima(), oldPassword, newPassword);
            y.setMima(newPassword);
            yishengMapper.updateById(y);
        } else {
            Huanzhe h = huanzheMapper.selectById(user.getId());
            checkPassword(h.getMima(), oldPassword, newPassword);
            h.setMima(newPassword);
            huanzheMapper.updateById(h);
        }
        return Result.success("修改成功", null);
    }

    /** 科室下拉（公开） */
    @GetMapping("/keshi")
    public Result<List<Keshi>> keshi() {
        return Result.success(keshiMapper.selectList(null));
    }

    /** 医保类型下拉（公开） */
    @GetMapping("/yibaoleixing")
    public Result<List<Yibaoleixing>> yibaoleixing() {
        return Result.success(yibaoleixingMapper.selectList(null));
    }

    private void checkPassword(String real, String oldPassword, String newPassword) {
        if (!real.equals(oldPassword)) {
            throw new BusinessException("原密码错误");
        }
        if (oldPassword.equals(newPassword)) {
            throw new BusinessException("新密码与旧密码一致");
        }
    }
}
