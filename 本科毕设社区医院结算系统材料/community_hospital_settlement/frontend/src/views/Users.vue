<template>
  <div>
    <el-card shadow="never">
      <el-form :inline="true" :model="query" @submit.prevent>
        <el-form-item label="用户名">
          <el-input v-model="query.username" placeholder="用户名" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="load">查询</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
      <div class="toolbar">
        <el-button type="primary" icon="Plus" @click="openAdd">添加</el-button>
      </div>
      <el-table :data="list" v-loading="loading" border stripe>
        <el-table-column prop="username" label="用户名" min-width="200" />
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" @click="openEdit(row)">修改</el-button>
            <el-button link type="danger" @click="remove(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="420px">
      <el-form :model="form" label-width="90px">
        <el-form-item label="用户名" required>
          <el-input v-model="form.username" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" show-password />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="save">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import request from '../utils/request'
import { useUserStore } from '../store/user'

const userStore = useUserStore()
const list = ref([])
const loading = ref(false)
const query = reactive({ username: '' })
const dialogVisible = ref(false)
const emptyForm = () => ({ id: null, username: '', password: '' })
const form = reactive(emptyForm())
const dialogTitle = computed(() => (form.id ? '修改' : '添加'))

async function load() {
  loading.value = true
  try {
    const res = await request.get(`/${userStore.prefix}/users`, { params: query })
    list.value = res.data
  } finally {
    loading.value = false
  }
}
function reset() {
  query.username = ''
  load()
}
function openAdd() {
  Object.assign(form, emptyForm())
  dialogVisible.value = true
}
function openEdit(row) {
  Object.assign(form, emptyForm(), row)
  form.password = ''
  dialogVisible.value = true
}
async function save() {
  if (!form.username) {
    ElMessage.warning('请填写用户名')
    return
  }
  const base = `/${userStore.prefix}/users`
  if (form.id) await request.put(`${base}/${form.id}`, form)
  else await request.post(base, form)
  ElMessage.success('保存成功')
  dialogVisible.value = false
  load()
}
async function remove(row) {
  await ElMessageBox.confirm('确定删除该管理员账号吗？', '提示', { type: 'warning' })
  await request.delete(`/${userStore.prefix}/users/${row.id}`)
  ElMessage.success('删除成功')
  load()
}

onMounted(load)
</script>

<style scoped>
.toolbar {
  margin-bottom: 12px;
}
</style>
