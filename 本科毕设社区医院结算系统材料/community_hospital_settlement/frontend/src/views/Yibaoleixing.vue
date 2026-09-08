<template>
  <div>
    <el-card shadow="never">
      <el-form :inline="true" :model="query" @submit.prevent>
        <el-form-item label="医保类型">
          <el-input v-model="query.yibaoleixing" placeholder="医保类型" clearable @keyup.enter="load" />
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
        <el-table-column prop="yibaoleixing" label="医保类型" min-width="200" />
        <el-table-column label="报销比例" width="140">
          <template #default="{ row }">{{ percent(row.baoxiaobili) }}</template>
        </el-table-column>
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" @click="openView(row)">查看</el-button>
            <el-button link type="primary" @click="openEdit(row)">修改</el-button>
            <el-button link type="danger" @click="remove(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="480px">
      <el-form :model="form" label-width="110px">
        <el-form-item label="医保类型" required>
          <el-input v-model="form.yibaoleixing" :disabled="isView" />
        </el-form-item>
        <el-form-item label="报销比例" required>
          <el-input-number v-model="form.baoxiaobili" :min="0" :max="1" :step="0.1" :precision="2" :disabled="isView" />
          <div class="tip">0.8 表示报销 80%</div>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button v-if="!isView" type="primary" @click="save">保存</el-button>
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
const query = reactive({ yibaoleixing: '' })
const dialogVisible = ref(false)
const isView = ref(false)
const emptyForm = () => ({ id: null, yibaoleixing: '', baoxiaobili: 0.8 })
const form = reactive(emptyForm())
const dialogTitle = computed(() => (isView.value ? '查看详情' : form.id ? '修改' : '添加'))

function percent(v) {
  if (v === null || v === undefined) return '-'
  return Math.round(v * 100) + '%'
}

async function load() {
  loading.value = true
  try {
    const res = await request.get(`/${userStore.prefix}/yibaoleixing`, { params: query })
    list.value = res.data
  } finally {
    loading.value = false
  }
}
function reset() {
  query.yibaoleixing = ''
  load()
}
function openAdd() {
  Object.assign(form, emptyForm())
  isView.value = false
  dialogVisible.value = true
}
function openEdit(row) {
  Object.assign(form, emptyForm(), row)
  isView.value = false
  dialogVisible.value = true
}
function openView(row) {
  Object.assign(form, emptyForm(), row)
  isView.value = true
  dialogVisible.value = true
}
async function save() {
  if (!form.yibaoleixing) {
    ElMessage.warning('请填写医保类型')
    return
  }
  const base = `/${userStore.prefix}/yibaoleixing`
  if (form.id) await request.put(`${base}/${form.id}`, form)
  else await request.post(base, form)
  ElMessage.success('保存成功')
  dialogVisible.value = false
  load()
}
async function remove(row) {
  await ElMessageBox.confirm('确定删除该医保类型吗？', '提示', { type: 'warning' })
  await request.delete(`/${userStore.prefix}/yibaoleixing/${row.id}`)
  ElMessage.success('删除成功')
  load()
}

onMounted(load)
</script>

<style scoped>
.toolbar {
  margin-bottom: 12px;
}
.tip {
  font-size: 12px;
  color: #909399;
  margin-top: 4px;
}
</style>
