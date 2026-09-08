package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.common.Result;
import com.community.entity.Huanzhe;
import com.community.mapper.HuanzheMapper;
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
 * 患者信息（管理员）
 */
@RestController
@RequestMapping("/api/admin/huanzhe")
public class AdminHuanzheController {

    private final HuanzheMapper huanzheMapper;

    public AdminHuanzheController(HuanzheMapper huanzheMapper) {
        this.huanzheMapper = huanzheMapper;
    }

    @GetMapping
    public Result<List<Huanzhe>> list(@RequestParam(required = false) String huanzhezhanghao,
                                      @RequestParam(required = false) String huanzhexingming,
                                      @RequestParam(required = false) Integer bingfanghao) {
        LambdaQueryWrapper<Huanzhe> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(huanzhezhanghao), Huanzhe::getHuanzhezhanghao, huanzhezhanghao)
          .like(StringUtils.hasText(huanzhexingming), Huanzhe::getHuanzhexingming, huanzhexingming)
          .eq(bingfanghao != null, Huanzhe::getBingfanghao, bingfanghao)
          .orderByDesc(Huanzhe::getId);
        return Result.success(huanzheMapper.selectList(qw));
    }

    @PostMapping
    public Result<Void> create(@RequestBody Huanzhe huanzhe) {
        Long count = huanzheMapper.selectCount(new LambdaQueryWrapper<Huanzhe>()
                .eq(Huanzhe::getHuanzhezhanghao, huanzhe.getHuanzhezhanghao()));
        if (count != null && count > 0) {
            throw new BusinessException("该患者账号已存在");
        }
        huanzheMapper.insert(huanzhe);
        return Result.success("新增成功", null);
    }

    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id, @RequestBody Huanzhe huanzhe) {
        huanzhe.setId(id);
        huanzheMapper.updateById(huanzhe);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        huanzheMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
