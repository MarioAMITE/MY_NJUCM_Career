<template>
  <el-container class="layout">
    <el-aside width="220px" class="aside">
      <div class="logo">
        <el-icon><FirstAidKit /></el-icon>
        <span>社区医院结算系统</span>
      </div>
      <el-menu
        :default-active="activeMenu"
        router
        background-color="#1f2d3d"
        text-color="#c0c4cc"
        active-text-color="#ffffff"
      >
        <el-menu-item v-for="m in menus" :key="m.path" :index="m.path">
          <el-icon><component :is="m.icon" /></el-icon>
          <span>{{ m.title }}</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header class="header">
        <div class="header-title">{{ currentTitle }}</div>
        <div class="header-right">
          <el-dropdown @command="handleCommand">
            <span class="user-info">
              <el-icon><UserFilled /></el-icon>
              {{ userStore.realName || userStore.username }}
              <el-tag size="small" type="primary" class="role-tag">{{ roleText }}</el-tag>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="profile">个人资料</el-dropdown-item>
                <el-dropdown-item command="logout" divided>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
      <el-main class="main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessageBox } from 'element-plus'
import { useUserStore } from '../store/user'

const userStore = useUserStore()
const route = useRoute()
const router = useRouter()

const allMenus = [
  { path: '/dashboard', title: '系统首页', icon: 'HomeFilled', roles: null },
  { path: '/yisheng', title: '医生信息', icon: 'Avatar', roles: ['ADMIN'] },
  { path: '/huanzhe', title: '患者信息', icon: 'UserFilled', roles: ['ADMIN', 'DOCTOR'] },
  { path: '/keshi', title: '科室信息', icon: 'OfficeBuilding', roles: ['ADMIN'] },
  { path: '/yaopin', title: '药品信息', icon: 'FirstAidKit', roles: ['ADMIN', 'DOCTOR'] },
  { path: '/yiliaofuwu', title: '医疗服务', icon: 'Stamp', roles: ['ADMIN', 'DOCTOR'] },
  { path: '/yibaoleixing', title: '医保类型', icon: 'Tickets', roles: ['ADMIN'] },
  { path: '/users', title: '管理员账号', icon: 'Setting', roles: ['ADMIN'] },
  { path: '/yaopinfeiyong', title: '药品费用', icon: 'Money', roles: null },
  { path: '/yiliaofeiyong', title: '医疗费用', icon: 'Wallet', roles: null },
  { path: '/profile', title: '个人资料', icon: 'User', roles: null }
]

const menus = computed(() => allMenus.filter((m) => !m.roles || m.roles.includes(userStore.role)))
const activeMenu = computed(() => route.path)
const currentTitle = computed(() => route.meta.title || '社区医院结算系统')
const roleText = computed(() => {
  const map = { ADMIN: '管理员', DOCTOR: '医生', PATIENT: '患者' }
  return map[userStore.role] || userStore.role
})

function handleCommand(cmd) {
  if (cmd === 'profile') {
    router.push('/profile')
  } else if (cmd === 'logout') {
    ElMessageBox.confirm('确定要退出登录吗？', '提示', { type: 'warning' }).then(() => {
      userStore.logout()
      router.push('/login')
    }).catch(() => {})
  }
}
</script>

<style scoped>
.layout {
  height: 100%;
}
.aside {
  background: #1f2d3d;
  overflow-x: hidden;
}
.logo {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
  background: #172433;
}
.logo .el-icon {
  font-size: 22px;
  color: #409eff;
}
.aside .el-menu {
  border-right: none;
}
.header {
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  height: 60px;
}
.header-title {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
}
.user-info {
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  color: #303133;
}
.role-tag {
  margin-left: 4px;
}
.main {
  background: #f0f4f8;
  padding: 16px;
}
</style>
