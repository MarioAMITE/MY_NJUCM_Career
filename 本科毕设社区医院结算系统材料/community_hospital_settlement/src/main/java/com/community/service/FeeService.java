package com.community.service;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.community.common.BusinessException;
import com.community.dto.DrugFeeCreateDTO;
import com.community.dto.MedicalFeeCreateDTO;
import com.community.entity.Huanzhe;
import com.community.entity.Yaopinfeiyong;
import com.community.entity.Yaopinxinxi;
import com.community.entity.Yibaoleixing;
import com.community.entity.Yiliaofeiyong;
import com.community.entity.Yiliaofuwu;
import com.community.mapper.HuanzheMapper;
import com.community.mapper.YaopinfeiyongMapper;
import com.community.mapper.YaopinxinxiMapper;
import com.community.mapper.YibaoleixingMapper;
import com.community.mapper.YiliaofeiyongMapper;
import com.community.mapper.YiliaofuwuMapper;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * 费用结算服务：下单（自动算价 + 医保报销扣减）与支付
 */
@Service
public class FeeService {

    private final YaopinfeiyongMapper yaopinfeiyongMapper;
    private final YiliaofeiyongMapper yiliaofeiyongMapper;
    private final YaopinxinxiMapper yaopinxinxiMapper;
    private final YiliaofuwuMapper yiliaofuwuMapper;
    private final YibaoleixingMapper yibaoleixingMapper;
    private final HuanzheMapper huanzheMapper;

    public FeeService(YaopinfeiyongMapper yaopinfeiyongMapper, YiliaofeiyongMapper yiliaofeiyongMapper,
                      YaopinxinxiMapper yaopinxinxiMapper, YiliaofuwuMapper yiliaofuwuMapper,
                      YibaoleixingMapper yibaoleixingMapper, HuanzheMapper huanzheMapper) {
        this.yaopinfeiyongMapper = yaopinfeiyongMapper;
        this.yiliaofeiyongMapper = yiliaofeiyongMapper;
        this.yaopinxinxiMapper = yaopinxinxiMapper;
        this.yiliaofuwuMapper = yiliaofuwuMapper;
        this.yibaoleixingMapper = yibaoleixingMapper;
        this.huanzheMapper = huanzheMapper;
    }

    /**
     * 创建药品费用订单
     */
    @Transactional
    public Yaopinfeiyong createDrugFee(DrugFeeCreateDTO dto, String yishenggonghao) {
        checkPatient(dto.getHuanzhezhanghao());
        if (dto.getItems() == null || dto.getItems().isEmpty()) {
            throw new BusinessException("请至少勾选一种药品");
        }

        double total = 0;
        StringBuilder detail = new StringBuilder();
        for (DrugFeeCreateDTO.Item item : dto.getItems()) {
            Yaopinxinxi yp = yaopinxinxiMapper.selectById(item.getYaopinId());
            if (yp == null) {
                throw new BusinessException("药品不存在");
            }
            if (item.getShuliang() == null || item.getShuliang() <= 0) {
                throw new BusinessException("药品数量必须大于0");
            }
            if (yp.getYaopinshuliang() == null || yp.getYaopinshuliang() < item.getShuliang()) {
                throw new BusinessException("药品「" + yp.getYaopinmingcheng() + "」库存不足");
            }
            total += yp.getYaopinshoujia() * item.getShuliang();
            detail.append(yp.getYaopinmingcheng()).append("×").append(item.getShuliang()).append(", ");

            // 扣减库存
            yp.setYaopinshuliang(yp.getYaopinshuliang() - item.getShuliang());
            yaopinxinxiMapper.updateById(yp);
        }

        double baoxiao = calcBaoxiao(total, dto.getYibaoleixingId());

        Yaopinfeiyong fee = new Yaopinfeiyong();
        fee.setDingdanbianhao(genOrderNo());
        fee.setYishenggonghao(yishenggonghao);
        fee.setHuanzhezhanghao(dto.getHuanzhezhanghao());
        fee.setAllyaopinshoujia(round2(total));
        fee.setBeizhu(detail.toString());
        fee.setBaoxiaofeiyong(round2(baoxiao));
        fee.setShifujine(round2(total - baoxiao));
        fee.setIspay("未支付");
        yaopinfeiyongMapper.insert(fee);
        return fee;
    }

    /**
     * 创建医疗费用订单
     */
    @Transactional
    public Yiliaofeiyong createMedicalFee(MedicalFeeCreateDTO dto, String yishenggonghao) {
        checkPatient(dto.getHuanzhezhanghao());
        if (dto.getItemIds() == null || dto.getItemIds().isEmpty()) {
            throw new BusinessException("请至少勾选一项医疗服务");
        }

        double total = 0;
        StringBuilder detail = new StringBuilder();
        for (Long id : dto.getItemIds()) {
            Yiliaofuwu fw = yiliaofuwuMapper.selectById(id);
            if (fw == null) {
                throw new BusinessException("医疗服务不存在");
            }
            total += fw.getXiangmujiage();
            detail.append(fw.getXiangmumingcheng()).append(", ");
        }

        double baoxiao = calcBaoxiao(total, dto.getYibaoleixingId());

        Yiliaofeiyong fee = new Yiliaofeiyong();
        fee.setDingdanbianhao(genOrderNo());
        fee.setYishenggonghao(yishenggonghao);
        fee.setHuanzhezhanghao(dto.getHuanzhezhanghao());
        fee.setAllxiangmujiage(round2(total));
        fee.setBeizhu(detail.toString());
        fee.setBaoxiaofeiyong(round2(baoxiao));
        fee.setShifufeiyong(round2(total - baoxiao));
        fee.setIspay("未支付");
        yiliaofeiyongMapper.insert(fee);
        return fee;
    }

    /**
     * 支付药品费用
     */
    public void payDrugFee(Long id) {
        Yaopinfeiyong fee = yaopinfeiyongMapper.selectById(id);
        if (fee == null) {
            throw new BusinessException("订单不存在");
        }
        if ("已支付".equals(fee.getIspay())) {
            throw new BusinessException("该订单已支付");
        }
        fee.setIspay("已支付");
        yaopinfeiyongMapper.updateById(fee);
    }

    /**
     * 支付医疗费用
     */
    public void payMedicalFee(Long id) {
        Yiliaofeiyong fee = yiliaofeiyongMapper.selectById(id);
        if (fee == null) {
            throw new BusinessException("订单不存在");
        }
        if ("已支付".equals(fee.getIspay())) {
            throw new BusinessException("该订单已支付");
        }
        fee.setIspay("已支付");
        yiliaofeiyongMapper.updateById(fee);
    }

    private void checkPatient(String huanzhezhanghao) {
        Long count = huanzheMapper.selectCount(new LambdaQueryWrapper<Huanzhe>()
                .eq(Huanzhe::getHuanzhezhanghao, huanzhezhanghao));
        if (count == null || count == 0) {
            throw new BusinessException("患者账号不存在");
        }
    }

    private double calcBaoxiao(double total, Long yibaoleixingId) {
        if (yibaoleixingId == null) {
            return 0;
        }
        Yibaoleixing ybl = yibaoleixingMapper.selectById(yibaoleixingId);
        if (ybl == null || ybl.getBaoxiaobili() == null) {
            return 0;
        }
        return total * ybl.getBaoxiaobili();
    }

    private String genOrderNo() {
        return String.valueOf(System.currentTimeMillis());
    }

    private double round2(double v) {
        return Math.round(v * 100) / 100.0;
    }
}
