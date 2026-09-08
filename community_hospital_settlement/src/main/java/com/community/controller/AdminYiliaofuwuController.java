package com.community.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.Result;
import com.community.entity.Yiliaofuwu;
import com.community.mapper.YiliaofuwuMapper;
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
 * 医疗服务（管理员）
 */
@RestController
@RequestMapping("/api/admin/yiliaofuwu")
public class AdminYiliaofuwuController {

    private final YiliaofuwuMapper yiliaofuwuMapper;

    public AdminYiliaofuwuController(YiliaofuwuMapper yiliaofuwuMapper) {
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

    @PostMapping
    public Result<Void> create(@RequestBody Yiliaofuwu yiliaofuwu) {
        yiliaofuwuMapper.insert(yiliaofuwu);
        return Result.success("新增成功", null);
    }

    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id, @RequestBody Yiliaofuwu yiliaofuwu) {
        yiliaofuwu.setId(id);
        yiliaofuwuMapper.updateById(yiliaofuwu);
        return Result.success("修改成功", null);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        yiliaofuwuMapper.deleteById(id);
        return Result.success("删除成功", null);
    }
}
