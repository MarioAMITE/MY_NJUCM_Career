namespace 非酒精性脂肪肝健康管理APP.Forms
{
    partial class ForumForm
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.titleLabel = new System.Windows.Forms.Label();
            this.postListView = new System.Windows.Forms.ListView();
            this.newPostBtn = new System.Windows.Forms.Button();
            this.replyBtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // titleLabel
            //
            this.titleLabel.AutoSize = true;
            this.titleLabel.Font = new System.Drawing.Font("微软雅黑", 15F, System.Drawing.FontStyle.Bold);
            this.titleLabel.Location = new System.Drawing.Point(24, 20);
            this.titleLabel.Name = "titleLabel";
            this.titleLabel.TabIndex = 0;
            this.titleLabel.Text = "论坛 · 患者交流";
            //
            // postListView
            //
            this.postListView.Location = new System.Drawing.Point(24, 64);
            this.postListView.Name = "postListView";
            this.postListView.Size = new System.Drawing.Size(520, 360);
            this.postListView.TabIndex = 1;
            this.postListView.UseCompatibleStateImageBehavior = false;
            //
            // newPostBtn
            //
            this.newPostBtn.Location = new System.Drawing.Point(24, 440);
            this.newPostBtn.Name = "newPostBtn";
            this.newPostBtn.Size = new System.Drawing.Size(120, 34);
            this.newPostBtn.TabIndex = 2;
            this.newPostBtn.Text = "发帖";
            this.newPostBtn.UseVisualStyleBackColor = true;
            this.newPostBtn.Click += new System.EventHandler(this.newPostBtn_Click);
            //
            // replyBtn
            //
            this.replyBtn.Location = new System.Drawing.Point(160, 440);
            this.replyBtn.Name = "replyBtn";
            this.replyBtn.Size = new System.Drawing.Size(120, 34);
            this.replyBtn.TabIndex = 3;
            this.replyBtn.Text = "回帖";
            this.replyBtn.UseVisualStyleBackColor = true;
            this.replyBtn.Click += new System.EventHandler(this.replyBtn_Click);
            //
            // ForumForm
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(568, 496);
            this.Controls.Add(this.replyBtn);
            this.Controls.Add(this.newPostBtn);
            this.Controls.Add(this.postListView);
            this.Controls.Add(this.titleLabel);
            this.Name = "ForumForm";
            this.Text = "论坛";
            this.Load += new System.EventHandler(this.ForumForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.Label titleLabel;
        private System.Windows.Forms.ListView postListView;
        private System.Windows.Forms.Button newPostBtn;
        private System.Windows.Forms.Button replyBtn;
    }
}
