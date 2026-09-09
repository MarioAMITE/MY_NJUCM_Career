using System;
using System.Windows.Forms;

namespace 非酒精性脂肪肝健康管理APP.Forms
{
    /// <summary>咨询：医患在线交流。</summary>
    public partial class ConsultForm : Form
    {
        public ConsultForm()
        {
            InitializeComponent();
        }

        private void ConsultForm_Load(object sender, EventArgs e)
        {
            // TODO: 从 IConsultMessageRepository 加载历史消息
            // TODO: 加载医生列表
        }

        private void sendBtn_Click(object sender, EventArgs e)
        {
            // TODO: 调用 IConsultMessageRepository.Insert 保存并显示消息
        }
    }
}
