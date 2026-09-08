package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.common.Result;
import com.community.entity.Users;
import com.community.mapper.UsersMapper;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * 管理员账号（管理员）
 */
@RestController
@RequestMapping("/api/admin/users")
public class AdminUsersController {

    private final UsersMapper usersMapper;

    public AdminUsersController(UsersMapper usersMapper) {
        this.usersMapper = usersMapper;
    }

    @GetMapping
    public Result<List<Users>> list(@RequestParam(required = false) String username) {
        LambdaQueryWrapper<Users> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(username), Users::getUsername, username).orderByDesc(Users::getId);
        return Result.success(usersMapper.selectList(qw));
    }

    @PostMapping
    public Result<Void> create(@RequestBody Users users) {
        Long count = usersMapper.selectCount(new LambdaQueryWrapper<Users>()
                .eq(Users::getUsername, users.getUsername()));
        if (count != null && count > 0) {
            throw new BusinessException("该用户名已存在");
        }
        usersMapper.insert(users);
        return Result.success("新增成功", null);
    }

    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id, @RequestBody Users users) {
        users.setId(id);
        usersMapper.updateById(users);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        usersMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
