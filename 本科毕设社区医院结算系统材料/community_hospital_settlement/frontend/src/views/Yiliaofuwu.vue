<template>
  <div>
    <el-card shadow="never">
      <el-form :inline="true" :model="query" @submit.prevent>
        <el-form-item label="项目名称">
          <el-input v-model="query.xiangmumingcheng" placeholder="项目名称" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item label="分类">
          <el-input v-model="query.xiangmufenlei" placeholder="项目分类" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="load">查询</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
      <div class="toolbar" v-if="isAdmin">
        <el-button type="primary" icon="Plus" @click="openAdd">添加</el-button>
      </div>
      <el-table :data="list" v-loading="loading" border stripe>
        <el-table-column prop="xiangmumingcheng" label="项目名称" min-width="130" />
        <el-table-column prop="xiangmufenlei" label="分类" width="90" />
        <el-table-column prop="xiangmujiage" label="价格(元)" width="100" />
        <el-table-column prop="keyueshijian" label="可约时间" min-width="150" />
        <el-table-column prop="xiangmuneirong" label="项目内容" min-width="120" show-overflow-tooltip />
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" @click="openView(row)">查看</el-button>
            <template v-if="isAdmin">
              <el-button link type="primary" @click="openEdit(row)">修改</el-button>
              <el-button link type="danger" @click="remove(row)">删除</el-button>
            </template>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="560px">
      <el-form :model="form" label-width="90px">
        <el-form-item label="项目名称" required>
          <el-input v-model="form.xiangmumingcheng" :disabled="isView" />
        </el-form-item>
        <el-form-item label="分类">
          <el-input v-model="form.xiangmufenlei" :disabled="isView" />
        </el-form-item>
        <el-form-item label="价格(元)">
          <el-input-number v-model="form.xiangmujiage" :min="0" :precision="2" :disabled="isView" />
        </el-form-item>
        <el-form-item label="可约时间">
          <el-input v-model="form.keyueshijian" :disabled="isView" />
        </el-form-item>
        <el-form-item label="项目内容">
          <el-input v-model="form.xiangmuneirong" :disabled="isView" type="textarea" />
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
const isAdmin = computed(() => userStore.role === 'ADMIN')
const list = ref([])
const loading = ref(false)
const query = reactive({ xiangmumingcheng: '', xiangmufenlei: '' })
const dialogVisible = ref(false)
const isView = ref(false)
const emptyForm = () => ({
  id: null, xiangmumingcheng: '', xiangmufenlei: '', xiangmujiage: null,
  keyueshijian: '', xiangmuneirong: ''
})
const form = reactive(emptyForm())
const dialogTitle = computed(() => (isView.value ? '查看详情' : form.id ? '修改' : '添加'))

async function load() {
  loading.value = true
  try {
    const res = await request.get(`/${userStore.prefix}/yiliaofuwu`, { params: query })
    list.value = res.data
  } finally {
    loading.value = false
  }
}
function reset() {
  query.xiangmumingcheng = ''
  query.xiangmufenlei = ''
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
  if (!form.xiangmumingcheng) {
    ElMessage.warning('请填写项目名称')
    return
  }
  const base = `/${userStore.prefix}/yiliaofuwu`
  if (form.id) await request.put(`${base}/${form.id}`, form)
  else await request.post(base, form)
  ElMessage.success('保存成功')
  dialogVisible.value = false
  load()
}
async function remove(row) {
  await ElMessageBox.confirm('确定删除该项目吗？', '提示', { type: 'warning' })
  await request.delete(`/${userStore.prefix}/yiliaofuwu/${row.id}`)
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
