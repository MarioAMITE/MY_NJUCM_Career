namespace 非酒精性脂肪肝健康管理APP.Forms
{
    partial class AiForm
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
            this.imgLabel = new System.Windows.Forms.Label();
            this.imagePathBox = new System.Windows.Forms.TextBox();
            this.browseBtn = new System.Windows.Forms.Button();
            this.descLabel = new System.Windows.Forms.Label();
            this.foodDescBox = new System.Windows.Forms.TextBox();
            this.analyzeBtn = new System.Windows.Forms.Button();
            this.resultLabel = new System.Windows.Forms.Label();
            this.resultBox = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            //
            // titleLabel
            //
            this.titleLabel.AutoSize = true;
            this.titleLabel.Font = new System.Drawing.Font("微软雅黑", 15F, System.Drawing.FontStyle.Bold);
            this.titleLabel.Location = new System.Drawing.Point(24, 16);
            this.titleLabel.Name = "titleLabel";
            this.titleLabel.TabIndex = 0;
            this.titleLabel.Text = "智能AI · 饮食分析";
            //
            // imgLabel
            //
            this.imgLabel.AutoSize = true;
            this.imgLabel.Location = new System.Drawing.Point(24, 62);
            this.imgLabel.Name = "imgLabel";
            this.imgLabel.TabIndex = 1;
            this.imgLabel.Text = "饮食图片：";
            //
            // imagePathBox
            //
            this.imagePathBox.Location = new System.Drawing.Point(110, 58);
            this.imagePathBox.Name = "imagePathBox";
            this.imagePathBox.Size = new System.Drawing.Size(280, 26);
            this.imagePathBox.TabIndex = 2;
            //
            // browseBtn
            //
            this.browseBtn.Location = new System.Drawing.Point(402, 56);
            this.browseBtn.Name = "browseBtn";
            this.browseBtn.Size = new System.Drawing.Size(100, 28);
            this.browseBtn.TabIndex = 3;
            this.browseBtn.Text = "选择图片";
            this.browseBtn.UseVisualStyleBackColor = true;
            this.browseBtn.Click += new System.EventHandler(this.browseBtn_Click);
            //
            // descLabel
            //
            this.descLabel.AutoSize = true;
            this.descLabel.Location = new System.Drawing.Point(24, 100);
            this.descLabel.Name = "descLabel";
            this.descLabel.TabIndex = 4;
            this.descLabel.Text = "饮食描述：";
            //
            // foodDescBox
            //
            this.foodDescBox.Location = new System.Drawing.Point(24, 126);
            this.foodDescBox.Multiline = true;
            this.foodDescBox.Name = "foodDescBox";
            this.foodDescBox.Size = new System.Drawing.Size(520, 90);
            this.foodDescBox.TabIndex = 5;
            //
            // analyzeBtn
            //
            this.analyzeBtn.Location = new System.Drawing.Point(24, 228);
            this.analyzeBtn.Name = "analyzeBtn";
            this.analyzeBtn.Size = new System.Drawing.Size(120, 34);
            this.analyzeBtn.TabIndex = 6;
            this.analyzeBtn.Text = "开始分析";
            this.analyzeBtn.UseVisualStyleBackColor = true;
            this.analyzeBtn.Click += new System.EventHandler(this.analyzeBtn_Click);
            //
            // resultLabel
            //
            this.resultLabel.AutoSize = true;
            this.resultLabel.Location = new System.Drawing.Point(24, 274);
            this.resultLabel.Name = "resultLabel";
            this.resultLabel.TabIndex = 7;
            this.resultLabel.Text = "分析结果：";
            //
            // resultBox
            //
            this.resultBox.Location = new System.Drawing.Point(24, 300);
            this.resultBox.Multiline = true;
            this.resultBox.Name = "resultBox";
            this.resultBox.ReadOnly = true;
            this.resultBox.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.resultBox.Size = new System.Drawing.Size(520, 160);
            this.resultBox.TabIndex = 8;
            //
            // AiForm
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(568, 480);
            this.Controls.Add(this.resultBox);
            this.Controls.Add(this.resultLabel);
            this.Controls.Add(this.analyzeBtn);
            this.Controls.Add(this.foodDescBox);
            this.Controls.Add(this.descLabel);
            this.Controls.Add(this.browseBtn);
            this.Controls.Add(this.imagePathBox);
            this.Controls.Add(this.imgLabel);
            this.Controls.Add(this.titleLabel);
            this.Name = "AiForm";
            this.Text = "智能AI";
            this.Load += new System.EventHandler(this.AiForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.Label titleLabel;
        private System.Windows.Forms.Label imgLabel;
        private System.Windows.Forms.TextBox imagePathBox;
        private System.Windows.Forms.Button browseBtn;
        private System.Windows.Forms.Label descLabel;
        private System.Windows.Forms.TextBox foodDescBox;
        private System.Windows.Forms.Button analyzeBtn;
        private System.Windows.Forms.Label resultLabel;
        private System.Windows.Forms.TextBox resultBox;
    }
}
