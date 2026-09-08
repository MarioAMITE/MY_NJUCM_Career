import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    id: localStorage.getItem('id') || '',
    username: localStorage.getItem('username') || '',
    role: localStorage.getItem('role') || '',
    realName: localStorage.getItem('realName') || ''
  }),
  getters: {
    isLogin: (state) => !!state.token,
    // 角色对应接口前缀：admin / doctor / patient
    prefix: (state) => (state.role ? state.role.toLowerCase() : '')
  },
  actions: {
    setLogin(data) {
      this.token = data.token
      this.id = data.id
      this.username = data.username
      this.role = data.role
      this.realName = data.realName || ''
      localStorage.setItem('token', data.token)
      localStorage.setItem('id', String(data.id ?? ''))
      localStorage.setItem('username', data.username)
      localStorage.setItem('role', data.role)
      localStorage.setItem('realName', data.realName || '')
    },
    logout() {
      this.token = ''
      this.id = ''
      this.username = ''
      this.role = ''
      this.realName = ''
      localStorage.clear()
    }
  }
})
