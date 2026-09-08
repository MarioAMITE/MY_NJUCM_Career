import axios from 'axios'
import { ElMessage } from 'element-plus'
import router from '../router'

const request = axios.create({
  baseURL: '/api',
  timeout: 15000
})

// 请求拦截：附带 token
request.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = 'Bearer ' + token
  }
  return config
})

// 响应拦截：统一处理 {code, message, data}
request.interceptors.response.use(
  (response) => {
    // 文件流（导出）直接返回原始响应
    if (response.config.responseType === 'blob') {
      return response
    }
    const res = response.data
    if (res.code === 200) {
      return res
    }
    ElMessage.error(res.message || '操作失败')
    return Promise.reject(new Error(res.message || '操作失败'))
  },
  (error) => {
    const status = error.response?.status
    const msg = error.response?.data?.message
    if (status === 401) {
      ElMessage.error(msg || '未登录或登录已失效')
      localStorage.clear()
      router.push('/login')
    } else if (status === 403) {
      ElMessage.error(msg || '权限不足')
    } else {
      ElMessage.error(msg || error.message || '网络错误')
    }
    return Promise.reject(error)
  }
)

export default request
