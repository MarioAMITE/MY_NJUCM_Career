package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.common.Result;
import com.community.entity.Yaopinfeiyong;
import com.community.entity.Yiliaofeiyong;
import com.community.mapper.YaopinfeiyongMapper;
import com.community.mapper.YiliaofeiyongMapper;
import com.community.security.UserContext;
import com.community.service.FeeService;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * 费用结算（患者，仅本人查看/支付）
 */
@RestController
@RequestMapping("/api/patient/feiyong")
public class PatientFeiyongController {

    private final FeeService feeService;
    private final YaopinfeiyongMapper yaopinfeiyongMapper;
    private final YiliaofeiyongMapper yiliaofeiyongMapper;

    public PatientFeiyongController(FeeService feeService, YaopinfeiyongMapper yaopinfeiyongMapper,
                                    YiliaofeiyongMapper yiliaofeiyongMapper) {
        this.feeService = feeService;
        this.yaopinfeiyongMapper = yaopinfeiyongMapper;
        this.yiliaofeiyongMapper = yiliaofeiyongMapper;
    }

    /* ---------------- 药品费用 ---------------- */

    @GetMapping("/yaopin")
    public Result<List<Yaopinfeiyong>> listYaopin(@RequestParam(required = false) String ispay) {
        LambdaQueryWrapper<Yaopinfeiyong> qw = new LambdaQueryWrapper<>();
        qw.eq(Yaopinfeiyong::getHuanzhezhanghao, UserContext.get().getUsername())
          .eq(StringUtils.hasText(ispay), Yaopinfeiyong::getIspay, ispay)
          .orderByDesc(Yaopinfeiyong::getId);
        return Result.success(yaopinfeiyongMapper.selectList(qw));
    }

    @PutMapping("/yaopin/{id}/pay")
    public Result<Void> payYaopin(@PathVariable Long id) {
        Yaopinfeiyong fee = yaopinfeiyongMapper.selectById(id);
        checkOwn(fee, fee == null ? null : fee.getHuanzhezhanghao());
        feeService.payDrugFee(id);
        return Result.success("支付成功", null);
    }

    /* ---------------- 医疗费用 ---------------- */

    @GetMapping("/yiliaofeiyong")
    public Result<List<Yiliaofeiyong>> listYiliaofeiyong(@RequestParam(required = false) String ispay) {
        LambdaQueryWrapper<Yiliaofeiyong> qw = new LambdaQueryWrapper<>();
        qw.eq(Yiliaofeiyong::getHuanzhezhanghao, UserContext.get().getUsername())
          .eq(StringUtils.hasText(ispay), Yiliaofeiyong::getIspay, ispay)
          .orderByDesc(Yiliaofeiyong::getId);
        return Result.success(yiliaofeiyongMapper.selectList(qw));
    }

    @PutMapping("/yiliaofeiyong/{id}/pay")
    public Result<Void> payYiliaofeiyong(@PathVariable Long id) {
        Yiliaofeiyong fee = yiliaofeiyongMapper.selectById(id);
        checkOwn(fee, fee == null ? null : fee.getHuanzhezhanghao());
        feeService.payMedicalFee(id);
        return Result.success("支付成功", null);
    }

    private void checkOwn(Object fee, String huanzhezhanghao) {
        if (fee == null) {
            throw new BusinessException("订单不存在");
        }
        if (!UserContext.get().getUsername().equals(huanzhezhanghao)) {
            throw new BusinessException("无权操作他人订单");
        }
    }
}
