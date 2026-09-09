namespace 非酒精性脂肪肝健康管理APP.Forms
{
    partial class ConsultForm
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
            this.doctorLabel = new System.Windows.Forms.Label();
            this.doctorList = new System.Windows.Forms.ListBox();
            this.chatBox = new System.Windows.Forms.TextBox();
            this.inputBox = new System.Windows.Forms.TextBox();
            this.sendBtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // titleLabel
            //
            this.titleLabel.AutoSize = true;
            this.titleLabel.Font = new System.Drawing.Font("微软雅黑", 15F, System.Drawing.FontStyle.Bold);
            this.titleLabel.Location = new System.Drawing.Point(24, 16);
            this.titleLabel.Name = "titleLabel";
            this.titleLabel.TabIndex = 0;
            this.titleLabel.Text = "咨询 · 医患交流";
            //
            // doctorLabel
            //
            this.doctorLabel.AutoSize = true;
            this.doctorLabel.Location = new System.Drawing.Point(24, 60);
            this.doctorLabel.Name = "doctorLabel";
            this.doctorLabel.TabIndex = 1;
            this.doctorLabel.Text = "医生列表：";
            //
            // doctorList
            //
            this.doctorList.FormattingEnabled = true;
            this.doctorList.Location = new System.Drawing.Point(24, 86);
            this.doctorList.Name = "doctorList";
            this.doctorList.Size = new System.Drawing.Size(160, 260);
            this.doctorList.TabIndex = 2;
            //
            // chatBox
            //
            this.chatBox.Location = new System.Drawing.Point(200, 60);
            this.chatBox.Multiline = true;
            this.chatBox.Name = "chatBox";
            this.chatBox.ReadOnly = true;
            this.chatBox.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.chatBox.Size = new System.Drawing.Size(344, 286);
            this.chatBox.TabIndex = 3;
            //
            // inputBox
            //
            this.inputBox.Location = new System.Drawing.Point(24, 360);
            this.inputBox.Multiline = true;
            this.inputBox.Name = "inputBox";
            this.inputBox.Size = new System.Drawing.Size(420, 60);
            this.inputBox.TabIndex = 4;
            //
            // sendBtn
            //
            this.sendBtn.Location = new System.Drawing.Point(460, 372);
            this.sendBtn.Name = "sendBtn";
            this.sendBtn.Size = new System.Drawing.Size(84, 36);
            this.sendBtn.TabIndex = 5;
            this.sendBtn.Text = "发送";
            this.sendBtn.UseVisualStyleBackColor = true;
            this.sendBtn.Click += new System.EventHandler(this.sendBtn_Click);
            //
            // ConsultForm
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(568, 440);
            this.Controls.Add(this.sendBtn);
            this.Controls.Add(this.inputBox);
            this.Controls.Add(this.chatBox);
            this.Controls.Add(this.doctorList);
            this.Controls.Add(this.doctorLabel);
            this.Controls.Add(this.titleLabel);
            this.Name = "ConsultForm";
            this.Text = "咨询";
            this.Load += new System.EventHandler(this.ConsultForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.Label titleLabel;
        private System.Windows.Forms.Label doctorLabel;
        private System.Windows.Forms.ListBox doctorList;
        private System.Windows.Forms.TextBox chatBox;
        private System.Windows.Forms.TextBox inputBox;
        private System.Windows.Forms.Button sendBtn;
    }
}
