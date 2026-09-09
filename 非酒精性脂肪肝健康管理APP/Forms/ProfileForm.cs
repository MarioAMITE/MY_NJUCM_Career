using System;
using System.Windows.Forms;

namespace 非酒精性脂肪肝健康管理APP.Forms
{
    /// <summary>个人中心：档案、指标与健康报告。</summary>
    public partial class ProfileForm : Form
    {
        public ProfileForm()
        {
            InitializeComponent();
            InitGrid();
        }

        private void InitGrid()
        {
            indicatorGrid.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            indicatorGrid.Columns.Add("指标", "指标");
            indicatorGrid.Columns.Add("数值", "数值");
            indicatorGrid.Columns.Add("参考范围", "参考范围");
        }

        private void ProfileForm_Load(object sender, EventArgs e)
        {
            // TODO: 从 IPatientRepository 加载个人档案（basicInfoLabel、indicatorGrid）
            // TODO: 从 IBehaviorLogRepository 加载行为日志，绘制指标趋势
        }

        private void exportBtn_Click(object sender, EventArgs e)
        {
            // TODO: 导出健康报告（PDF / 文本）
        }
    }
}
