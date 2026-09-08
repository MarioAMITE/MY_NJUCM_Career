package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.Result;
import com.community.dto.DrugFeeCreateDTO;
import com.community.dto.MedicalFeeCreateDTO;
import com.community.entity.Yaopinfeiyong;
import com.community.entity.Yiliaofeiyong;
import com.community.mapper.YaopinfeiyongMapper;
import com.community.mapper.YiliaofeiyongMapper;
import com.community.security.UserContext;
import com.community.service.FeeService;
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
 * 费用结算（管理员，全量）
 */
@RestController
@RequestMapping("/api/admin/feiyong")
public class AdminFeiyongController {

    private final FeeService feeService;
    private final YaopinfeiyongMapper yaopinfeiyongMapper;
    private final YiliaofeiyongMapper yiliaofeiyongMapper;

    public AdminFeiyongController(FeeService feeService, YaopinfeiyongMapper yaopinfeiyongMapper,
                                  YiliaofeiyongMapper yiliaofeiyongMapper) {
        this.feeService = feeService;
        this.yaopinfeiyongMapper = yaopinfeiyongMapper;
        this.yiliaofeiyongMapper = yiliaofeiyongMapper;
    }

    /* ---------------- 药品费用 ---------------- */

    @GetMapping("/yaopin")
    public Result<List<Yaopinfeiyong>> listYaopin(@RequestParam(required = false) String ispay,
                                                  @RequestParam(required = false) String huanzhezhanghao,
                                                  @RequestParam(required = false) String yishenggonghao) {
        LambdaQueryWrapper<Yaopinfeiyong> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(huanzhezhanghao), Yaopinfeiyong::getHuanzhezhanghao, huanzhezhanghao)
          .like(StringUtils.hasText(yishenggonghao), Yaopinfeiyong::getYishenggonghao, yishenggonghao)
          .eq(StringUtils.hasText(ispay), Yaopinfeiyong::getIspay, ispay)
          .orderByDesc(Yaopinfeiyong::getId);
        return Result.success(yaopinfeiyongMapper.selectList(qw));
    }

    @PostMapping("/yaopin")
    public Result<Void> createYaopin(@RequestBody DrugFeeCreateDTO dto) {
        feeService.createDrugFee(dto, UserContext.get().getUsername());
        return Result.success("下单成功", null);
    }

    @PutMapping("/yaopin/{id}")
    public Result<Void> updateYaopin(@PathVariable Long id, @RequestBody Yaopinfeiyong fee) {
        fee.setId(id);
        yaopinfeiyongMapper.updateById(fee);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/yaopin/{id}")
    public Result<Void> deleteYaopin(@PathVariable Long id) {
        yaopinfeiyongMapper.deleteById(id);
        return Result.success("删除成功", null);
    }

    /* ---------------- 医疗费用 ---------------- */

    @GetMapping("/yiliaofeiyong")
    public Result<List<Yiliaofeiyong>> listYiliaofeiyong(@RequestParam(required = false) String ispay,
                                                         @RequestParam(required = false) String huanzhezhanghao,
                                                         @RequestParam(required = false) String yishenggonghao) {
        LambdaQueryWrapper<Yiliaofeiyong> qw = new LambdaQueryWrapper<>();
        qw.like(StringUtils.hasText(huanzhezhanghao), Yiliaofeiyong::getHuanzhezhanghao, huanzhezhanghao)
          .like(StringUtils.hasText(yishenggonghao), Yiliaofeiyong::getYishenggonghao, yishenggonghao)
          .eq(StringUtils.hasText(ispay), Yiliaofeiyong::getIspay, ispay)
          .orderByDesc(Yiliaofeiyong::getId);
        return Result.success(yiliaofeiyongMapper.selectList(qw));
    }

    @PostMapping("/yiliaofeiyong")
    public Result<Void> createYiliaofeiyong(@RequestBody MedicalFeeCreateDTO dto) {
        feeService.createMedicalFee(dto, UserContext.get().getUsername());
        return Result.success("下单成功", null);
    }

    @PutMapping("/yiliaofeiyong/{id}")
    public Result<Void> updateYiliaofeiyong(@PathVariable Long id, @RequestBody Yiliaofeiyong fee) {
        fee.setId(id);
        yiliaofeiyongMapper.updateById(fee);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/yiliaofeiyong/{id}")
    public Result<Void> deleteYiliaofeiyong(@PathVariable Long id) {
        yiliaofeiyongMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
