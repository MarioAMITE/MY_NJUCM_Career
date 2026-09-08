<template>
  <div>
    <el-card shadow="never">
      <el-form :inline="true" :model="query" @submit.prevent>
        <el-form-item label="支付状态">
          <el-select v-model="query.ispay" placeholder="全部" clearable style="width: 140px" @change="load">
            <el-option label="未支付" value="未支付" />
            <el-option label="已支付" value="已支付" />
          </el-select>
        </el-form-item>
        <el-form-item v-if="canManage" label="患者账号">
          <el-input v-model="query.huanzhezhanghao" placeholder="患者账号" clearable @keyup.enter="load" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="load">查询</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
      <div class="toolbar">
        <el-button v-if="canManage" type="primary" icon="Plus" @click="openCreate">下单</el-button>
        <el-button icon="Download" @click="exportExcel">导出</el-button>
      </div>
      <el-table :data="list" v-loading="loading" border stripe>
        <el-table-column prop="dingdanbianhao" label="订单编号" width="150" />
        <el-table-column prop="yishenggonghao" label="医生工号" width="100" />
        <el-table-column prop="huanzhezhanghao" label="患者账号" width="100" />
        <el-table-column prop="allyaopinshoujia" label="药费总金额" width="110" />
        <el-table-column prop="baoxiaofeiyong" label="报销费用" width="100" />
        <el-table-column prop="shifujine" label="实付金额" width="100" />
        <el-table-column prop="beizhu" label="药品明细" min-width="160" show-overflow-tooltip />
        <el-table-column label="支付状态" width="100">
          <template #default="{ row }">
            <el-tag :type="row.ispay === '已支付' ? 'success' : 'warning'" size="small">{{ row.ispay }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="240" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" @click="openReceipt(row)">查看</el-button>
            <template v-if="canManage">
              <el-button link type="primary" @click="openEdit(row)">修改</el-button>
              <el-button link type="danger" @click="remove(row)">删除</el-button>
            </template>
            <el-button v-if="isPatient && row.ispay !== '已支付'" link type="success" @click="pay(row)">支付</el-button>
            <el-button link @click="openReceipt(row, true)">打印</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 下单对话框 -->
    <el-dialog v-model="createDialog.visible" title="药品费用下单" width="760px">
      <el-form label-width="90px">
        <el-form-item label="患者" required>
          <el-select v-model="createDialog.huanzhezhanghao" placeholder="选择患者" filterable style="width: 300px">
            <el-option
              v-for="p in patientOptions"
              :key="p.huanzhezhanghao"
              :label="p.huanzhezhanghao + ' - ' + p.huanzhexingming"
              :value="p.huanzhezhanghao"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="勾选药品">
          <el-table :data="drugOptions" border size="small" max-height="280">
            <el-table-column label="选择" width="60">
              <template #default="{ row }">
                <el-checkbox v-model="row.checked" />
              </template>
            </el-table-column>
            <el-table-column prop="yaopinmingcheng" label="药品名称" min-width="140" />
            <el-table-column prop="yaopinshoujia" label="售价(元)" width="100" />
            <el-table-column label="数量" width="140">
              <template #default="{ row }">
                <el-input-number v-model="row.shuliang" :min="1" :max="row.yaopinshuliang" :disabled="!row.checked" size="small" />
              </template>
            </el-table-column>
          </el-table>
        </el-form-item>
        <el-form-item label="医保类型">
          <el-select v-model="createDialog.yibaoleixingId" placeholder="选择医保类型（可留空）" clearable style="width: 300px">
            <el-option
              v-for="y in yibaoleixingOptions"
              :key="y.id"
              :label="y.yibaoleixing + '（报销' + percent(y.baoxiaobili) + '）'"
              :value="y.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="费用预览">
          <div class="preview">
            总金额：<b>¥{{ total.toFixed(2) }}</b>
            &nbsp;&nbsp;报销：<b class="green">-¥{{ baoxiao.toFixed(2) }}</b>
            &nbsp;&nbsp;实付：<b class="red">¥{{ shifu.toFixed(2) }}</b>
          </div>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="createDialog.visible = false">取消</el-button>
        <el-button type="primary" @click="submitCreate">确认下单</el-button>
      </template>
    </el-dialog>

    <!-- 修改对话框 -->
    <el-dialog v-model="editDialog.visible" title="修改药品费用" width="520px">
      <el-form :model="editDialog.form" label-width="100px">
        <el-form-item label="订单编号">
          <el-input :model-value="editDialog.form.dingdanbianhao" disabled />
        </el-form-item>
        <el-form-item label="报销费用">
          <el-input-number v-model="editDialog.form.baoxiaofeiyong" :min="0" :precision="2" />
        </el-form-item>
        <el-form-item label="实付金额">
          <el-input-number v-model="editDialog.form.shifujine" :min="0" :precision="2" />
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="editDialog.form.beizhu" type="textarea" />
        </el-form-item>
        <el-form-item label="支付状态">
          <el-radio-group v-model="editDialog.form.ispay">
            <el-radio label="未支付">未支付</el-radio>
            <el-radio label="已支付">已支付</el-radio>
          </el-radio-group>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="editDialog.visible = false">取消</el-button>
        <el-button type="primary" @click="submitEdit">保存</el-button>
      </template>
    </el-dialog>

    <!-- 查看/打印 -->
    <el-dialog v-model="receiptVisible" title="费用单" width="520px">
      <div class="print-receipt">
        <h3 class="receipt-title">社区医院药品费用单</h3>
        <el-descriptions :column="2" border>
          <el-descriptions-item label="订单编号">{{ receipt.dingdanbianhao }}</el-descriptions-item>
          <el-descriptions-item label="支付状态">{{ receipt.ispay }}</el-descriptions-item>
          <el-descriptions-item label="医生工号">{{ receipt.yishenggonghao }}</el-descriptions-item>
          <el-descriptions-item label="患者账号">{{ receipt.huanzhezhanghao }}</el-descriptions-item>
          <el-descriptions-item label="药费总金额">¥{{ receipt.allyaopinshoujia }}</el-descriptions-item>
          <el-descriptions-item label="报销费用">¥{{ receipt.baoxiaofeiyong }}</el-descriptions-item>
          <el-descriptions-item label="实付金额">¥{{ receipt.shifujine }}</el-descriptions-item>
          <el-descriptions-item label="药品明细" :span="2">{{ receipt.beizhu }}</el-descriptions-item>
        </el-descriptions>
      </div>
      <template #footer>
        <el-button @click="receiptVisible = false">关闭</el-button>
        <el-button type="primary" @click="printReceipt">打印</el-button>
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
const isDoctor = computed(() => userStore.role === 'DOCTOR')
const isPatient = computed(() => userStore.role === 'PATIENT')
const canManage = computed(() => isAdmin.value || isDoctor.value)
const base = computed(() => `/${userStore.prefix}/feiyong/yaopin`)

const list = ref([])
const loading = ref(false)
const query = reactive({ ispay: '', huanzhezhanghao: '' })

const patientOptions = ref([])
const drugOptions = ref([])
const yibaoleixingOptions = ref([])
const createDialog = reactive({ visible: false, huanzhezhanghao: '', yibaoleixingId: null })

const total = computed(() =>
  drugOptions.value.filter((d) => d.checked).reduce((s, d) => s + (d.yaopinshoujia || 0) * (d.shuliang || 0), 0)
)
const baoxiao = computed(() => {
  const y = yibaoleixingOptions.value.find((x) => x.id === createDialog.yibaoleixingId)
  return total.value * (y ? y.baoxiaobili || 0 : 0)
})
const shifu = computed(() => total.value - baoxiao.value)

const editDialog = reactive({ visible: false, form: {} })
const receiptVisible = ref(false)
const receipt = ref({})

function percent(v) {
  if (v === null || v === undefined) return '-'
  return Math.round(v * 100) + '%'
}

async function load() {
  loading.value = true
  try {
    const res = await request.get(base.value, { params: query })
    list.value = res.data
  } finally {
    loading.value = false
  }
}

function reset() {
  query.ispay = ''
  query.huanzhezhanghao = ''
  load()
}

async function openCreate() {
  const [patients, drugs, ybl] = await Promise.all([
    request.get(`/${userStore.prefix}/huanzhe`),
    request.get(`/${userStore.prefix}/yaopin`),
    request.get('/common/yibaoleixing')
  ])
  patientOptions.value = patients.data || []
  drugOptions.value = (drugs.data || []).map((d) => ({ ...d, checked: false, shuliang: 1 }))
  yibaoleixingOptions.value = ybl.data || []
  createDialog.huanzhezhanghao = ''
  createDialog.yibaoleixingId = null
  createDialog.visible = true
}

async function submitCreate() {
  if (!createDialog.huanzhezhanghao) {
    ElMessage.warning('请选择患者')
    return
  }
  const items = drugOptions.value.filter((d) => d.checked).map((d) => ({ yaopinId: d.id, shuliang: d.shuliang }))
  if (!items.length) {
    ElMessage.warning('请至少勾选一种药品')
    return
  }
  await request.post(base.value, {
    huanzhezhanghao: createDialog.huanzhezhanghao,
    yibaoleixingId: createDialog.yibaoleixingId,
    items
  })
  ElMessage.success('下单成功')
  createDialog.visible = false
  load()
}

function openEdit(row) {
  editDialog.form = { ...row }
  editDialog.visible = true
}

async function submitEdit() {
  await request.put(`${base.value}/${editDialog.form.id}`, editDialog.form)
  ElMessage.success('修改成功')
  editDialog.visible = false
  load()
}

async function remove(row) {
  await ElMessageBox.confirm('确定删除该订单吗？', '提示', { type: 'warning' })
  await request.delete(`${base.value}/${row.id}`)
  ElMessage.success('删除成功')
  load()
}

async function pay(row) {
  await ElMessageBox.confirm(`确认支付该订单（实付 ¥${row.shifujine}）？`, '支付确认', { type: 'warning' })
  await request.put(`${base.value}/${row.id}/pay`)
  ElMessage.success('支付成功')
  load()
}

function openReceipt(row, toPrint = false) {
  receipt.value = row
  receiptVisible.value = true
  if (toPrint) {
    setTimeout(() => printReceipt(), 300)
  }
}

function printReceipt() {
  window.print()
}

async function exportExcel() {
  const response = await request.get('/export/yaopinfeiyong', { responseType: 'blob' })
  const url = window.URL.createObjectURL(new Blob([response.data]))
  const a = document.createElement('a')
  a.href = url
  a.download = '药品费用.xlsx'
  a.click()
  window.URL.revokeObjectURL(url)
}

onMounted(load)
</script>

<style scoped>
.toolbar {
  margin-bottom: 12px;
}
.preview {
  font-size: 15px;
}
.preview .green {
  color: #67c23a;
}
.preview .red {
  color: #f56c6c;
}
.receipt-title {
  text-align: center;
  margin: 0 0 16px;
}
</style>
