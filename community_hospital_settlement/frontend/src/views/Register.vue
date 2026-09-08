<template>
  <div class="register-page">
    <el-card class="register-card" shadow="always">
      <div class="title">
        <el-icon class="title-icon"><FirstAidKit /></el-icon>
        <h2>医生注册</h2>
      </div>
      <el-form :model="form" :rules="rules" ref="formRef" label-width="90px">
        <el-form-item label="工号" prop="yishenggonghao">
          <el-input v-model="form.yishenggonghao" placeholder="请输入医生工号" />
        </el-form-item>
        <el-form-item label="姓名" prop="yishengxingming">
          <el-input v-model="form.yishengxingming" placeholder="请输入姓名" />
        </el-form-item>
        <el-form-item label="密码" prop="mima">
          <el-input v-model="form.mima" type="password" show-password placeholder="请输入密码" />
        </el-form-item>
        <el-form-item label="职称">
          <el-input v-model="form.zhicheng" placeholder="如：主治医师" />
        </el-form-item>
        <el-form-item label="主治方向">
          <el-input v-model="form.zhuzhifangxiang" placeholder="请输入主治方向" />
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="form.xingbie">
            <el-radio label="男">男</el-radio>
            <el-radio label="女">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="科室">
          <el-input v-model="form.keshi" placeholder="请输入科室" />
        </el-form-item>
        <el-form-item label="联系电话" prop="lianxidianhua">
          <el-input v-model="form.lianxidianhua" placeholder="请输入11位手机号" />
        </el-form-item>
        <el-button type="primary" style="width: 100%" :loading="loading" @click="register">注 册</el-button>
        <div class="reg-link">
          <el-link type="primary" @click="$router.push('/login')">返回登录</el-link>
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

const router = useRouter()
const formRef = ref()
const loading = ref(false)
const form = reactive({
  yishenggonghao: '',
  yishengxingming: '',
  mima: '',
  zhicheng: '',
  zhuzhifangxiang: '',
  xingbie: '男',
  keshi: '',
  lianxidianhua: ''
})

const rules = {
  yishenggonghao: [{ required: true, message: '请输入医生工号', trigger: 'blur' }],
  yishengxingming: [{ required: true, message: '请输入姓名', trigger: 'blur' }],
  mima: [{ required: true, message: '请输入密码', trigger: 'blur' }],
  lianxidianhua: [
    { required: true, message: '请输入联系电话', trigger: 'blur' },
    { pattern: /^1\d{10}$/, message: '请输入正确的11位手机号', trigger: 'blur' }
  ]
}

async function register() {
  await formRef.value.validate()
  loading.value = true
  try {
    await request.post('/auth/register', form)
    ElMessage.success('注册成功，请登录')
    router.push('/login')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 0;
  background: linear-gradient(135deg, #1e6fb8 0%, #2f8fd6 50%, #63b3e6 100%);
}
.register-card {
  width: 460px;
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
