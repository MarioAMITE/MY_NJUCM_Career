<template>
  <div class="login-page">
    <el-card class="login-card" shadow="always">
      <div class="title">
        <el-icon class="title-icon"><FirstAidKit /></el-icon>
        <h2>社区医院结算系统</h2>
      </div>
      <el-form :model="form" label-position="top">
        <el-form-item label="账号">
          <el-input v-model="form.username" placeholder="请输入账号" clearable />
        </el-form-item>
        <el-form-item label="密码">
          <el-input
            v-model="form.password"
            type="password"
            show-password
            placeholder="请输入密码"
            @keyup.enter="login"
          />
        </el-form-item>
        <el-form-item label="角色">
          <el-select v-model="form.role" style="width: 100%">
            <el-option label="管理员" value="ADMIN" />
            <el-option label="医生" value="DOCTOR" />
            <el-option label="患者" value="PATIENT" />
          </el-select>
        </el-form-item>
        <el-button type="primary" style="width: 100%" :loading="loading" @click="login">登 录</el-button>
        <div class="reg-link">
          <el-link type="primary" @click="$router.push('/register')">医生注册</el-link>
        </div>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import request from '../utils/request'
import { useUserStore } from '../store/user'

const router = useRouter()
const userStore = useUserStore()
const loading = ref(false)
const form = reactive({ username: '', password: '', role: 'ADMIN' })

async function login() {
  if (!form.username || !form.password) {
    ElMessage.warning('请输入账号和密码')
    return
  }
  loading.value = true
  try {
    const res = await request.post('/auth/login', form)
    userStore.setLogin(res.data)
    ElMessage.success('登录成功')
    router.push('/dashboard')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #1e6fb8 0%, #2f8fd6 50%, #63b3e6 100%);
}
.login-card {
  width: 380px;
  padding: 10px 20px;
}
.title {
  text-align: center;
  margin-bottom: 20px;
}
.title-icon {
  font-size: 40px;
  color: #409eff;
}
.title h2 {
  margin: 8px 0 0;
  color: #303133;
}
.reg-link {
  text-align: center;
  margin-top: 14px;
}
</style>
