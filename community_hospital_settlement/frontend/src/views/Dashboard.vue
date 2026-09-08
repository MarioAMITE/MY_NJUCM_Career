<template>
  <div>
    <el-card shadow="never" class="welcome">
      <div class="welcome-inner">
        <el-icon class="welcome-icon"><FirstAidKit /></el-icon>
        <div>
          <h2>欢迎使用社区医院结算系统</h2>
          <p class="sub">{{ userStore.realName || userStore.username }}，欢迎回来！您当前的角色是「{{ roleText }}」。</p>
        </div>
      </div>
    </el-card>

    <el-row :gutter="16" class="cards">
      <el-col :span="8" v-for="c in cards" :key="c.title">
        <el-card shadow="hover" class="info-card">
          <div class="info-card-title">{{ c.title }}</div>
          <div class="info-card-desc">{{ c.desc }}</div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useUserStore } from '../store/user'

const userStore = useUserStore()
const roleText = computed(() => {
  const map = { ADMIN: '管理员', DOCTOR: '医生', PATIENT: '患者' }
  return map[userStore.role] || userStore.role
})

const cards = computed(() => {
  const all = [
    { title: '医生/患者管理', desc: '维护医生信息、患者建档，管理科室与医保类型。', roles: ['ADMIN', 'DOCTOR'] },
    { title: '药品与服务', desc: '维护药品信息、医疗服务项目，供医生开单勾选。', roles: ['ADMIN', 'DOCTOR'] },
    { title: '费用结算', desc: '医生开药品费/医疗费订单，按医保类型自动报销，患者在线支付。', roles: null },
    { title: '导出与打印', desc: '费用支持 Excel 导出与打印，方便对账归档。', roles: null }
  ]
  return all.filter((c) => !c.roles || c.roles.includes(userStore.role))
})
</script>

<style scoped>
.welcome {
  margin-bottom: 16px;
}
.welcome-inner {
  display: flex;
  align-items: center;
  gap: 20px;
}
.welcome-icon {
  font-size: 52px;
  color: #409eff;
}
.welcome h2 {
  margin: 0 0 8px;
  color: #303133;
}
.sub {
  margin: 0;
  color: #909399;
}
.cards {
  margin-top: 4px;
}
.info-card-title {
  font-size: 16px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 8px;
}
.info-card-desc {
  font-size: 13px;
  color: #909399;
  line-height: 1.6;
}
</style>
