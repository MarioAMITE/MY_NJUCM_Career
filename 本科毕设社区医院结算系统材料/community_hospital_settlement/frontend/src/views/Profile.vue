<template>
  <div>
    <el-row :gutter="16">
      <el-col :span="12">
        <el-card shadow="never" header="个人信息">
          <el-descriptions :column="1" border>
            <el-descriptions-item v-for="r in profileRows" :key="r.label" :label="r.label">
              {{ r.value }}
            </el-descriptions-item>
          </el-descriptions>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card shadow="never" header="修改密码">
          <el-form :model="pwdForm" :rules="pwdRules" ref="pwdRef" label-width="90px">
            <el-form-item label="原密码" prop="oldPassword">
              <el-input v-model="pwdForm.oldPassword" type="password" show-password />
            </el-form-item>
            <el-form-item label="新密码" prop="newPassword">
              <el-input v-model="pwdForm.newPassword" type="password" show-password />
            </el-form-item>
            <el-form-item label="确认新密码" prop="confirmPassword">
              <el-input v-model="pwdForm.confirmPassword" type="password" show-password />
            </el-form-item>
            <el-button type="primary" @click="changePassword">保存</el-button>
          </el-form>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import request from '../utils/request'
import { useUserStore } from '../store/user'

const userStore = useUserStore()
const pwdRef = ref()
const profileRows = ref([])

const pwdForm = reactive({ oldPassword: '', newPassword: '', confirmPassword: '' })
const pwdRules = {
  oldPassword: [{ required: true, message: '请输入原密码', trigger: 'blur' }],
  newPassword: [{ required: true, message: '请输入新密码', trigger: 'blur' }],
  confirmPassword: [
    { required: true, message: '请再次输入新密码', trigger: 'blur' },
    {
      validator: (rule, value, cb) => {
        if (value !== pwdForm.newPassword) cb(new Error('两次输入的密码不一致'))
        else cb()
      },
      trigger: 'blur'
    }
  ]
}

const LABELS = {
  username: '用户名',
  yishenggonghao: '医生工号',
  yishengxingming: '姓名',
  zhicheng: '职称',
  zhuzhifangxiang: '主治方向',
  xingbie: '性别',
  keshi: '科室',
  lianxidianhua: '联系电话',
  huanzhezhanghao: '患者账号',
  huanzhexingming: '姓名',
  xuexing: '血型',
  nianling: '年龄',
  shouji: '手机号',
  bingfanghao: '病房号',
  chuangweihao: '床位号',
  bingzheng: '病症',
  shenfenzheng: '身份证号'
}
const SKIP = ['id', 'mima', 'password', 'addtime', 'touxiang', 'image']

async function loadProfile() {
  const res = await request.get('/common/profile')
  const data = res.data || {}
  profileRows.value = Object.keys(data)
    .filter((k) => !SKIP.includes(k) && data[k] !== null && data[k] !== '')
    .map((k) => ({ label: LABELS[k] || k, value: data[k] }))
}

async function changePassword() {
  await pwdRef.value.validate()
  await request.put('/common/password', {
    oldPassword: pwdForm.oldPassword,
    newPassword: pwdForm.newPassword
  })
  ElMessage.success('密码修改成功')
  pwdForm.oldPassword = ''
  pwdForm.newPassword = ''
  pwdForm.confirmPassword = ''
}

onMounted(loadProfile)
</script>
