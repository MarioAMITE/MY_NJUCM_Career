package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.Result;
import com.community.entity.Yaopinxinxi;
import com.community.mapper.YaopinxinxiMapper;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * 药品信息（医生，只读查询）
 */
@RestController
@RequestMapping("/api/doctor/yaopin")
public class DoctorYaopinController {

    private final YaopinxinxiMapper yaopinxinxiMapper;

    public DoctorYaopinController(YaopinxinxiMapper yaopinxinxiMapper) {
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
}
