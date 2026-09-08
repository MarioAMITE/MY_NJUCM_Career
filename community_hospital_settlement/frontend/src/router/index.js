import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/login', component: () => import('../views/Login.vue'), meta: { title: '登录' } },
  { path: '/register', component: () => import('../views/Register.vue'), meta: { title: '医生注册' } },
  {
    path: '/',
    component: () => import('../layout/Layout.vue'),
    redirect: '/dashboard',
    children: [
      { path: 'dashboard', component: () => import('../views/Dashboard.vue'), meta: { title: '系统首页' } },
      { path: 'yisheng', component: () => import('../views/Yisheng.vue'), meta: { title: '医生信息', roles: ['ADMIN'] } },
      { path: 'huanzhe', component: () => import('../views/Huanzhe.vue'), meta: { title: '患者信息', roles: ['ADMIN', 'DOCTOR'] } },
      { path: 'keshi', component: () => import('../views/Keshi.vue'), meta: { title: '科室信息', roles: ['ADMIN'] } },
      { path: 'yaopin', component: () => import('../views/Yaopinxinxi.vue'), meta: { title: '药品信息', roles: ['ADMIN', 'DOCTOR'] } },
      { path: 'yiliaofuwu', component: () => import('../views/Yiliaofuwu.vue'), meta: { title: '医疗服务', roles: ['ADMIN', 'DOCTOR'] } },
      { path: 'yibaoleixing', component: () => import('../views/Yibaoleixing.vue'), meta: { title: '医保类型', roles: ['ADMIN'] } },
      { path: 'users', component: () => import('../views/Users.vue'), meta: { title: '管理员账号', roles: ['ADMIN'] } },
      { path: 'yaopinfeiyong', component: () => import('../views/Yaopinfeiyong.vue'), meta: { title: '药品费用' } },
      { path: 'yiliaofeiyong', component: () => import('../views/Yiliaofeiyong.vue'), meta: { title: '医疗费用' } },
      { path: 'profile', component: () => import('../views/Profile.vue'), meta: { title: '个人资料' } }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  const role = localStorage.getItem('role')
  if (to.path === '/login' || to.path === '/register') {
    next()
    return
  }
  if (!token) {
    next('/login')
    return
  }
  if (to.meta.roles && !to.meta.roles.includes(role)) {
    next('/dashboard')
    return
  }
  next()
})

export default router
