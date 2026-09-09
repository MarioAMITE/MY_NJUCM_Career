using System;
using System.Windows.Forms;

namespace 非酒精性脂肪肝健康管理APP.Forms
{
    /// <summary>智能AI：饮食图像识别与饮食分析。</summary>
    public partial class AiForm : Form
    {
        public AiForm()
        {
            InitializeComponent();
        }

        private void AiForm_Load(object sender, EventArgs e)
        {
        }

        private void browseBtn_Click(object sender, EventArgs e)
        {
            // 选择图片（真实交互）；识别逻辑预留 IDietImageRecognizer 接口
            using (var ofd = new OpenFileDialog())
            {
                ofd.Filter = "图片文件|*.jpg;*.jpeg;*.png;*.bmp";
                if (ofd.ShowDialog() == DialogResult.OK)
                {
                    imagePathBox.Text = ofd.FileName;
                }
            }
        }

        private void analyzeBtn_Click(object sender, EventArgs e)
        {
            // TODO: 调用 IDietAnalysisService.Analyze(foodDescBox.Text)
            // TODO: 将结果写入 ai_analysis_record 表
        }
    }
}
