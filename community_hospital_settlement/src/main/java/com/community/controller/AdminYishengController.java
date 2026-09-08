package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.common.Result;
import com.community.entity.Yisheng;
import com.community.mapper.YishengMapper;
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
 * 医生信息（管理员）
 */
@RestController
@RequestMapping("/api/admin/yisheng")
public class AdminYishengController {

    private final YishengMapper yishengMapper;

    public AdminYishengController(YishengMapper yishengMapper) {
        this.yishengMapper = yishengMapper;
    }

    @GetMapping
    public Result<List<Yisheng>> list(@RequestParam(required = false) String yishengxingming,
                                      @RequestParam(required = false) String zhicheng) {
        LambdaQueryWrapper<Yisheng> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(yishengxingming), Yisheng::getYishengxingming, yishengxingming)
          .like(StringUtils.hasText(zhicheng), Yisheng::getZhicheng, zhicheng)
          .orderByDesc(Yisheng::getId);
        return Result.success(yishengMapper.selectList(qw));
    }

    @PostMapping
    public Result<Void> create(@RequestBody Yisheng yisheng) {
        Long count = yishengMapper.selectCount(new LambdaQueryWrapper<Yisheng>()
                .eq(Yisheng::getYishenggonghao, yisheng.getYishenggonghao()));
        if (count != null && count > 0) {
            throw new BusinessException("该医生工号已存在");
        }
        yishengMapper.insert(yisheng);
        return Result.success("新增成功", null);
    }

    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id, @RequestBody Yisheng yisheng) {
        yisheng.setId(id);
        yishengMapper.updateById(yisheng);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        yishengMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
