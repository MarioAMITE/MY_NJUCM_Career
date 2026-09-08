<template>
  <div>
    <el-card shadow="never">
      <el-form :inline="true" :model="query" @submit.prevent>
        <el-form-item label="姓名">
          <el-input v-model="query.yishengxingming" placeholder="医生姓名" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item label="职称">
          <el-input v-model="query.zhicheng" placeholder="职称" clearable @keyup.enter="load" />
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
        <el-table-column prop="yishenggonghao" label="工号" width="100" />
        <el-table-column prop="yishengxingming" label="姓名" width="100" />
        <el-table-column prop="zhicheng" label="职称" width="120" />
        <el-table-column prop="zhuzhifangxiang" label="主治方向" width="110" />
        <el-table-column prop="xingbie" label="性别" width="70" />
        <el-table-column prop="keshi" label="科室" width="90" />
        <el-table-column prop="lianxidianhua" label="联系电话" min-width="130" />
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" @click="openView(row)">查看</el-button>
            <el-button link type="primary" @click="openEdit(row)">修改</el-button>
            <el-button link type="danger" @click="remove(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="560px">
      <el-form :model="form" label-width="90px">
        <el-form-item label="工号" required>
          <el-input v-model="form.yishenggonghao" :disabled="isView" placeholder="请输入医生工号" />
        </el-form-item>
        <el-form-item label="姓名" required>
          <el-input v-model="form.yishengxingming" :disabled="isView" placeholder="请输入姓名" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.mima" :disabled="isView" placeholder="登录密码" />
        </el-form-item>
        <el-form-item label="职称">
          <el-input v-model="form.zhicheng" :disabled="isView" placeholder="如：主治医师" />
        </el-form-item>
        <el-form-item label="主治方向">
          <el-input v-model="form.zhuzhifangxiang" :disabled="isView" />
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="form.xingbie" :disabled="isView">
            <el-radio label="男">男</el-radio>
            <el-radio label="女">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="科室">
          <el-input v-model="form.keshi" :disabled="isView" />
        </el-form-item>
        <el-form-item label="联系电话">
          <el-input v-model="form.lianxidianhua" :disabled="isView" placeholder="11位手机号" />
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
const query = reactive({ yishengxingming: '', zhicheng: '' })
const dialogVisible = ref(false)
const isView = ref(false)

const emptyForm = () => ({
  id: null, yishenggonghao: '', yishengxingming: '', mima: '', zhicheng: '',
  zhuzhifangxiang: '', xingbie: '男', keshi: '', lianxidianhua: ''
})
const form = reactive(emptyForm())
const dialogTitle = computed(() => (isView.value ? '查看详情' : form.id ? '修改' : '添加'))

async function load() {
  loading.value = true
  try {
    const res = await request.get(`/${userStore.prefix}/yisheng`, { params: query })
    list.value = res.data
  } finally {
    loading.value = false
  }
}

function reset() {
  query.yishengxingming = ''
  query.zhicheng = ''
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
  if (!form.yishenggonghao || !form.yishengxingming) {
    ElMessage.warning('请填写工号和姓名')
    return
  }
  const base = `/${userStore.prefix}/yisheng`
  if (form.id) await request.put(`${base}/${form.id}`, form)
  else await request.post(base, form)
  ElMessage.success('保存成功')
  dialogVisible.value = false
  load()
}

async function remove(row) {
  await ElMessageBox.confirm('确定删除该医生吗？', '提示', { type: 'warning' })
  await request.delete(`/${userStore.prefix}/yisheng/${row.id}`)
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
