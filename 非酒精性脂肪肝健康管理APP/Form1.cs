using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using 非酒精性脂肪肝健康管理APP.Forms;

namespace 非酒精性脂肪肝健康管理APP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 商城
        private void button1_Click(object sender, EventArgs e)
        {
            using (var f = new ShopForm()) { f.ShowDialog(this); }
        }

        // 论坛
        private void button2_Click(object sender, EventArgs e)
        {
            using (var f = new ForumForm()) { f.ShowDialog(this); }
        }

        // 智能AI
        private void button3_Click(object sender, EventArgs e)
        {
            using (var f = new AiForm()) { f.ShowDialog(this); }
        }

        // 咨询
        private void button4_Click(object sender, EventArgs e)
        {
            using (var f = new ConsultForm()) { f.ShowDialog(this); }
        }

        // 个人中心
        private void button5_Click(object sender, EventArgs e)
        {
            using (var f = new ProfileForm()) { f.ShowDialog(this); }
        }

        private void label1_Click(object sender, EventArgs e)
        {
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }
    }
}
