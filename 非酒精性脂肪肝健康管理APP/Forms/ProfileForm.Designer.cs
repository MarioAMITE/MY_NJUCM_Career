namespace 非酒精性脂肪肝健康管理APP.Forms
{
    partial class ProfileForm
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
            this.basicInfoLabel = new System.Windows.Forms.Label();
            this.indicatorGrid = new System.Windows.Forms.DataGridView();
            this.exportBtn = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.indicatorGrid)).BeginInit();
            this.SuspendLayout();
            //
            // titleLabel
            //
            this.titleLabel.AutoSize = true;
            this.titleLabel.Font = new System.Drawing.Font("微软雅黑", 15F, System.Drawing.FontStyle.Bold);
            this.titleLabel.Location = new System.Drawing.Point(24, 16);
            this.titleLabel.Name = "titleLabel";
            this.titleLabel.TabIndex = 0;
            this.titleLabel.Text = "个人中心";
            //
            // basicInfoLabel
            //
            this.basicInfoLabel.AutoSize = true;
            this.basicInfoLabel.Location = new System.Drawing.Point(24, 60);
            this.basicInfoLabel.Name = "basicInfoLabel";
            this.basicInfoLabel.TabIndex = 1;
            this.basicInfoLabel.Text = "姓名：——    年龄：——    BMI：——    诊断：非酒精性脂肪肝";
            //
            // indicatorGrid
            //
            this.indicatorGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.indicatorGrid.Location = new System.Drawing.Point(24, 96);
            this.indicatorGrid.Name = "indicatorGrid";
            this.indicatorGrid.Size = new System.Drawing.Size(520, 280);
            this.indicatorGrid.TabIndex = 2;
            //
            // exportBtn
            //
            this.exportBtn.Location = new System.Drawing.Point(24, 392);
            this.exportBtn.Name = "exportBtn";
            this.exportBtn.Size = new System.Drawing.Size(120, 34);
            this.exportBtn.TabIndex = 3;
            this.exportBtn.Text = "导出报告";
            this.exportBtn.UseVisualStyleBackColor = true;
            this.exportBtn.Click += new System.EventHandler(this.exportBtn_Click);
            //
            // ProfileForm
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(568, 448);
            this.Controls.Add(this.exportBtn);
            this.Controls.Add(this.indicatorGrid);
            this.Controls.Add(this.basicInfoLabel);
            this.Controls.Add(this.titleLabel);
            this.Name = "ProfileForm";
            this.Text = "个人中心";
            this.Load += new System.EventHandler(this.ProfileForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.indicatorGrid)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.Label titleLabel;
        private System.Windows.Forms.Label basicInfoLabel;
        private System.Windows.Forms.DataGridView indicatorGrid;
        private System.Windows.Forms.Button exportBtn;
    }
}
