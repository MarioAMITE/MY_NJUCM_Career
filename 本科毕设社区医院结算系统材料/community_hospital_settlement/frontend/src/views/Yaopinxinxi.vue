<template>
  <div>
    <el-card shadow="never">
      <el-form :inline="true" :model="query" @submit.prevent>
        <el-form-item label="药品名称">
          <el-input v-model="query.yaopinmingcheng" placeholder="药品名称" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item label="类别">
          <el-input v-model="query.yaopinleibie" placeholder="药品类别" clearable @keyup.enter="load" />
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
        <el-table-column prop="yaopinmingcheng" label="药品名称" min-width="140" />
        <el-table-column prop="yaopinleibie" label="类别" width="90" />
        <el-table-column prop="yongtu" label="用途" min-width="100" />
        <el-table-column prop="guige" label="规格" min-width="100" />
        <el-table-column prop="chandi" label="产地" width="90" />
        <el-table-column prop="yaopinshuliang" label="数量" width="80" />
        <el-table-column prop="yaopinshoujia" label="售价(元)" width="100" />
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
        <el-form-item label="药品名称" required>
          <el-input v-model="form.yaopinmingcheng" :disabled="isView" />
        </el-form-item>
        <el-form-item label="类别">
          <el-input v-model="form.yaopinleibie" :disabled="isView" />
        </el-form-item>
        <el-form-item label="用途">
          <el-input v-model="form.yongtu" :disabled="isView" />
        </el-form-item>
        <el-form-item label="规格">
          <el-input v-model="form.guige" :disabled="isView" />
        </el-form-item>
        <el-form-item label="产地">
          <el-input v-model="form.chandi" :disabled="isView" />
        </el-form-item>
        <el-form-item label="数量">
          <el-input-number v-model="form.yaopinshuliang" :min="0" :disabled="isView" />
        </el-form-item>
        <el-form-item label="售价(元)">
          <el-input-number v-model="form.yaopinshoujia" :min="0" :precision="2" :disabled="isView" />
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="form.beizhu" :disabled="isView" type="textarea" />
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
const query = reactive({ yaopinmingcheng: '', yaopinleibie: '' })
const dialogVisible = ref(false)
const isView = ref(false)
const emptyForm = () => ({
  id: null, yaopinmingcheng: '', yaopinleibie: '', yongtu: '', guige: '',
  chandi: '', yaopinshuliang: null, yaopinshoujia: null, beizhu: ''
})
const form = reactive(emptyForm())
const dialogTitle = computed(() => (isView.value ? '查看详情' : form.id ? '修改' : '添加'))

async function load() {
  loading.value = true
  try {
    const res = await request.get(`/${userStore.prefix}/yaopin`, { params: query })
    list.value = res.data
  } finally {
    loading.value = false
  }
}
function reset() {
  query.yaopinmingcheng = ''
  query.yaopinleibie = ''
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
  if (!form.yaopinmingcheng) {
    ElMessage.warning('请填写药品名称')
    return
  }
  const base = `/${userStore.prefix}/yaopin`
  if (form.id) await request.put(`${base}/${form.id}`, form)
  else await request.post(base, form)
  ElMessage.success('保存成功')
  dialogVisible.value = false
  load()
}
async function remove(row) {
  await ElMessageBox.confirm('确定删除该药品吗？', '提示', { type: 'warning' })
  await request.delete(`/${userStore.prefix}/yaopin/${row.id}`)
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
