package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.common.Result;
import com.community.entity.Yibaoleixing;
import com.community.mapper.YibaoleixingMapper;
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
 * 医保类型（管理员）
 */
@RestController
@RequestMapping("/api/admin/yibaoleixing")
public class AdminYibaoleixingController {

    private final YibaoleixingMapper yibaoleixingMapper;

    public AdminYibaoleixingController(YibaoleixingMapper yibaoleixingMapper) {
        this.yibaoleixingMapper = yibaoleixingMapper;
    }

    @GetMapping
    public Result<List<Yibaoleixing>> list(@RequestParam(required = false) String yibaoleixing) {
        LambdaQueryWrapper<Yibaoleixing> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(yibaoleixing), Yibaoleixing::getYibaoleixing, yibaoleixing)
          .orderByDesc(Yibaoleixing::getId);
        return Result.success(yibaoleixingMapper.selectList(qw));
    }

    @PostMapping
    public Result<Void> create(@RequestBody Yibaoleixing yibaoleixing) {
        Long count = yibaoleixingMapper.selectCount(new LambdaQueryWrapper<Yibaoleixing>()
                .eq(Yibaoleixing::getYibaoleixing, yibaoleixing.getYibaoleixing()));
        if (count != null && count > 0) {
            throw new BusinessException("该医保类型已存在");
        }
        yibaoleixingMapper.insert(yibaoleixing);
        return Result.success("新增成功", null);
    }

    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id, @RequestBody Yibaoleixing yibaoleixing) {
        yibaoleixing.setId(id);
        yibaoleixingMapper.updateById(yibaoleixing);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        yibaoleixingMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
