package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.Result;
import com.community.entity.Yiliaofuwu;
import com.community.mapper.YiliaofuwuMapper;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * 医疗服务（医生，只读查询）
 */
@RestController
@RequestMapping("/api/doctor/yiliaofuwu")
public class DoctorYiliaofuwuController {

    private final YiliaofuwuMapper yiliaofuwuMapper;

    public DoctorYiliaofuwuController(YiliaofuwuMapper yiliaofuwuMapper) {
        this.yiliaofuwuMapper = yiliaofuwuMapper;
    }

    @GetMapping
    public Result<List<Yiliaofuwu>> list(@RequestParam(required = false) String xiangmumingcheng,
                                         @RequestParam(required = false) String xiangmufenlei) {
        LambdaQueryWrapper<Yiliaofuwu> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(xiangmumingcheng), Yiliaofuwu::getXiangmumingcheng, xiangmumingcheng)
          .like(StringUtils.hasText(xiangmufenlei), Yiliaofuwu::getXiangmufenlei, xiangmufenlei)
          .orderByDesc(Yiliaofuwu::getId);
        return Result.success(yiliaofuwuMapper.selectList(qw));
    }
}
