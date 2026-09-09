using System;
using System.Windows.Forms;

namespace 非酒精性脂肪肝健康管理APP.Forms
{
    /// <summary>论坛：患者交流与经验分享。</summary>
    public partial class ForumForm : Form
    {
        public ForumForm()
        {
            InitializeComponent();
            InitPostList();
        }

        private void InitPostList()
        {
            postListView.View = View.Details;
            postListView.FullRowSelect = true;
            postListView.GridLines = true;
            postListView.Columns.Add("标题", 240);
            postListView.Columns.Add("板块", 100);
            postListView.Columns.Add("作者", 80);
            postListView.Columns.Add("时间", 130);
        }

        private void ForumForm_Load(object sender, EventArgs e)
        {
            // TODO: 从 IPostRepository 加载帖子列表
        }

        private void newPostBtn_Click(object sender, EventArgs e)
        {
            // TODO: 打开发帖窗体，写入 post 表
        }

        private void replyBtn_Click(object sender, EventArgs e)
        {
            // TODO: 打开回帖窗体，写入 reply 表
        }
    }
}
