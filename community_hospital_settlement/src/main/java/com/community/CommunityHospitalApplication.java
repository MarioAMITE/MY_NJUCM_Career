package com.community;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * 社区医院结算系统启动类
 */
@SpringBootApplication
@MapperScan("com.community.mapper")
public class CommunityHospitalApplication {

    public static void main(String[] args) {
        SpringApplication.run(CommunityHospitalApplication.class, args);
    }
}
