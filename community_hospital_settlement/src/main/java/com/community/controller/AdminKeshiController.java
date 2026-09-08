package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.common.Result;
import com.community.entity.Keshi;
import com.community.mapper.KeshiMapper;
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
 * 科室信息（管理员）
 */
@RestController
@RequestMapping("/api/admin/keshi")
public class AdminKeshiController {

    private final KeshiMapper keshiMapper;

    public AdminKeshiController(KeshiMapper keshiMapper) {
        this.keshiMapper = keshiMapper;
    }

    @GetMapping
    public Result<List<Keshi>> list(@RequestParam(required = false) String keshi) {
        LambdaQueryWrapper<Keshi> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(keshi), Keshi::getKeshi, keshi).orderByDesc(Keshi::getId);
        return Result.success(keshiMapper.selectList(qw));
    }

    @PostMapping
    public Result<Void> create(@RequestBody Keshi keshi) {
        Long count = keshiMapper.selectCount(new LambdaQueryWrapper<Keshi>()
                .eq(Keshi::getKeshi, keshi.getKeshi()));
        if (count != null && count > 0) {
            throw new BusinessException("该科室已存在");
        }
        keshiMapper.insert(keshi);
        return Result.success("新增成功", null);
    }

    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id, @RequestBody Keshi keshi) {
        keshi.setId(id);
        keshiMapper.updateById(keshi);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        keshiMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
