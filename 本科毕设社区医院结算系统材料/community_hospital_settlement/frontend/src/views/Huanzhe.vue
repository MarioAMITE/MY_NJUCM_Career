<template>
  <div>
    <el-card shadow="never">
      <el-form :inline="true" :model="query" @submit.prevent>
        <el-form-item label="患者账号">
          <el-input v-model="query.huanzhezhanghao" placeholder="患者账号" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="query.huanzhexingming" placeholder="患者姓名" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item label="病房号">
          <el-input-number v-model="query.bingfanghao" :min="0" placeholder="病房号" controls-position="right" />
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
        <el-table-column prop="huanzhezhanghao" label="患者账号" width="110" />
        <el-table-column prop="huanzhexingming" label="姓名" width="100" />
        <el-table-column prop="xuexing" label="血型" width="70" />
        <el-table-column prop="xingbie" label="性别" width="70" />
        <el-table-column prop="nianling" label="年龄" width="70" />
        <el-table-column prop="shouji" label="手机" min-width="120" />
        <el-table-column prop="bingfanghao" label="病房号" width="80" />
        <el-table-column prop="chuangweihao" label="床位号" width="80" />
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" @click="openView(row)">查看</el-button>
            <el-button link type="primary" @click="openEdit(row)">修改</el-button>
            <el-button link type="danger" @click="remove(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="640px">
      <el-form :model="form" label-width="90px">
        <el-form-item label="患者账号" required>
          <el-input v-model="form.huanzhezhanghao" :disabled="isView" />
        </el-form-item>
        <el-form-item label="姓名" required>
          <el-input v-model="form.huanzhexingming" :disabled="isView" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.mima" :disabled="isView" />
        </el-form-item>
        <el-form-item label="血型">
          <el-select v-model="form.xuexing" :disabled="isView" style="width: 100%">
            <el-option label="A" value="A" />
            <el-option label="B" value="B" />
            <el-option label="AB" value="AB" />
            <el-option label="O" value="O" />
          </el-select>
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="form.xingbie" :disabled="isView">
            <el-radio label="男">男</el-radio>
            <el-radio label="女">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input-number v-model="form.nianling" :min="0" :max="150" :disabled="isView" />
        </el-form-item>
        <el-form-item label="手机">
          <el-input v-model="form.shouji" :disabled="isView" />
        </el-form-item>
        <el-form-item label="病房号">
          <el-input-number v-model="form.bingfanghao" :min="0" :disabled="isView" />
        </el-form-item>
        <el-form-item label="床位号">
          <el-input-number v-model="form.chuangweihao" :min="0" :disabled="isView" />
        </el-form-item>
        <el-form-item label="病症">
          <el-input v-model="form.bingzheng" :disabled="isView" type="textarea" />
        </el-form-item>
        <el-form-item label="身份证">
          <el-input v-model="form.shenfenzheng" :disabled="isView" />
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
const query = reactive({ huanzhezhanghao: '', huanzhexingming: '', bingfanghao: null })
const dialogVisible = ref(false)
const isView = ref(false)

const emptyForm = () => ({
  id: null, huanzhezhanghao: '', huanzhexingming: '', mima: '', xuexing: 'A',
  xingbie: '男', nianling: null, shouji: '', bingfanghao: null, chuangweihao: null,
  bingzheng: '', shenfenzheng: ''
})
const form = reactive(emptyForm())
const dialogTitle = computed(() => (isView.value ? '查看详情' : form.id ? '修改' : '添加'))

async function load() {
  loading.value = true
  try {
    const res = await request.get(`/${userStore.prefix}/huanzhe`, { params: query })
    list.value = res.data
  } finally {
    loading.value = false
  }
}

function reset() {
  query.huanzhezhanghao = ''
  query.huanzhexingming = ''
  query.bingfanghao = null
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
  if (!form.huanzhezhanghao || !form.huanzhexingming) {
    ElMessage.warning('请填写患者账号和姓名')
    return
  }
  const base = `/${userStore.prefix}/huanzhe`
  if (form.id) await request.put(`${base}/${form.id}`, form)
  else await request.post(base, form)
  ElMessage.success('保存成功')
  dialogVisible.value = false
  load()
}

async function remove(row) {
  await ElMessageBox.confirm('确定删除该患者吗？', '提示', { type: 'warning' })
  await request.delete(`/${userStore.prefix}/huanzhe/${row.id}`)
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
