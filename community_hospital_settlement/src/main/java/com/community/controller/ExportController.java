package com.community.controller;

import com.alibaba.excel.EasyExcel;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.entity.Yaopinfeiyong;
import com.community.entity.Yiliaofeiyong;
import com.community.mapper.YaopinfeiyongMapper;
import com.community.mapper.YiliaofeiyongMapper;
import com.community.security.LoginUser;
import com.community.security.UserContext;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Excel 导出（按角色范围：管理员全量 / 医生本人 / 患者本人）
 */
@RestController
@RequestMapping("/api/export")
public class ExportController {

    private final YaopinfeiyongMapper yaopinfeiyongMapper;
    private final YiliaofeiyongMapper yiliaofeiyongMapper;

    public ExportController(YaopinfeiyongMapper yaopinfeiyongMapper,
                            YiliaofeiyongMapper yiliaofeiyongMapper) {
        this.yaopinfeiyongMapper = yaopinfeiyongMapper;
        this.yiliaofeiyongMapper = yiliaofeiyongMapper;
    }

    @GetMapping("/yaopinfeiyong")
    public void exportYaopinfeiyong(HttpServletResponse response) throws IOException {
        LambdaQueryWrapper<Yaopinfeiyong> qw = scopeDrug();
        List<Yaopinfeiyong> list = yaopinfeiyongMapper.selectList(qw);

        List<List<String>> head = head("订单编号", "医生工号", "患者账号", "药费总金额", "报销费用", "实付金额", "备注", "是否支付");
        List<List<Object>> rows = new ArrayList<>();
        for (Yaopinfeiyong f : list) {
            rows.add(Arrays.asList(
                    f.getDingdanbianhao(), f.getYishenggonghao(), f.getHuanzhezhanghao(),
                    f.getAllyaopinshoujia(), f.getBaoxiaofeiyong(), f.getShifujine(),
                    f.getBeizhu(), f.getIspay()));
        }
        write(response, "药品费用", head, rows);
    }

    @GetMapping("/yiliaofeiyong")
    public void exportYiliaofeiyong(HttpServletResponse response) throws IOException {
        LambdaQueryWrapper<Yiliaofeiyong> qw = scopeMedical();
        List<Yiliaofeiyong> list = yiliaofeiyongMapper.selectList(qw);

        List<List<String>> head = head("订单编号", "医生工号", "患者账号", "项目总金额", "报销费用", "实付费用", "备注", "是否支付");
        List<List<Object>> rows = new ArrayList<>();
        for (Yiliaofeiyong f : list) {
            rows.add(Arrays.asList(
                    f.getDingdanbianhao(), f.getYishenggonghao(), f.getHuanzhezhanghao(),
                    f.getAllxiangmujiage(), f.getBaoxiaofeiyong(), f.getShifufeiyong(),
                    f.getBeizhu(), f.getIspay()));
        }
        write(response, "医疗费用", head, rows);
    }

    private LambdaQueryWrapper<Yaopinfeiyong> scopeDrug() {
        LoginUser user = UserContext.get();
        LambdaQueryWrapper<Yaopinfeiyong> qw = new LambdaQueryWrapper<>();
        if ("DOCTOR".equals(user.getRole())) {
            qw.eq(Yaopinfeiyong::getYishenggonghao, user.getUsername());
        } else if ("PATIENT".equals(user.getRole())) {
            qw.eq(Yaopinfeiyong::getHuanzhezhanghao, user.getUsername());
        }
        qw.orderByDesc(Yaopinfeiyong::getId);
        return qw;
    }

    private LambdaQueryWrapper<Yiliaofeiyong> scopeMedical() {
        LoginUser user = UserContext.get();
        LambdaQueryWrapper<Yiliaofeiyong> qw = new LambdaQueryWrapper<>();
        if ("DOCTOR".equals(user.getRole())) {
            qw.eq(Yiliaofeiyong::getYishenggonghao, user.getUsername());
        } else if ("PATIENT".equals(user.getRole())) {
            qw.eq(Yiliaofeiyong::getHuanzhezhanghao, user.getUsername());
        }
        qw.orderByDesc(Yiliaofeiyong::getId);
        return qw;
    }

    private List<List<String>> head(String... titles) {
        List<List<String>> head = new ArrayList<>();
        for (String t : titles) {
            head.add(Collections.singletonList(t));
        }
        return head;
    }

    private void write(HttpServletResponse response, String fileName,
                       List<List<String>> head, List<List<Object>> rows) throws IOException {
        response.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
        response.setCharacterEncoding("utf-8");
        String encoded = URLEncoder.encode(fileName, StandardCharsets.UTF_8.name()).replaceAll("\\+", "%20");
        response.setHeader("Content-disposition", "attachment;filename*=utf-8''" + encoded + ".xlsx");
        EasyExcel.write(response.getOutputStream()).head(head).sheet(fileName).doWrite(rows);
    }
}
