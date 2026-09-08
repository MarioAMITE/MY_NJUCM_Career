package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.Result;
import com.community.entity.Yaopinxinxi;
import com.community.mapper.YaopinxinxiMapper;
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
 * 药品信息（管理员）
 */
@RestController
@RequestMapping("/api/admin/yaopin")
public class AdminYaopinController {

    private final YaopinxinxiMapper yaopinxinxiMapper;

    public AdminYaopinController(YaopinxinxiMapper yaopinxinxiMapper) {
        this.yaopinxinxiMapper = yaopinxinxiMapper;
    }

    @GetMapping
    public Result<List<Yaopinxinxi>> list(@RequestParam(required = false) String yaopinmingcheng,
                                          @RequestParam(required = false) String yaopinleibie) {
        LambdaQueryWrapper<Yaopinxinxi> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(yaopinmingcheng), Yaopinxinxi::getYaopinmingcheng, yaopinmingcheng)
          .like(StringUtils.hasText(yaopinleibie), Yaopinxinxi::getYaopinleibie, yaopinleibie)
          .orderByDesc(Yaopinxinxi::getId);
        return Result.success(yaopinxinxiMapper.selectList(qw));
    }

    @PostMapping
    public Result<Void> create(@RequestBody Yaopinxinxi yaopinxinxi) {
        yaopinxinxiMapper.insert(yaopinxinxi);
        return Result.success("新增成功", null);
    }

    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id, @RequestBody Yaopinxinxi yaopinxinxi) {
        yaopinxinxi.setId(id);
        yaopinxinxiMapper.updateById(yaopinxinxi);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        yaopinxinxiMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
