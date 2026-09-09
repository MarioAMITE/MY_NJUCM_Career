namespace 非酒精性脂肪肝健康管理APP.Forms
{
    partial class ShopForm
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
            this.searchBox = new System.Windows.Forms.TextBox();
            this.searchBtn = new System.Windows.Forms.Button();
            this.productListView = new System.Windows.Forms.ListView();
            this.addCartBtn = new System.Windows.Forms.Button();
            this.viewCartBtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // titleLabel
            //
            this.titleLabel.AutoSize = true;
            this.titleLabel.Font = new System.Drawing.Font("微软雅黑", 15F, System.Drawing.FontStyle.Bold);
            this.titleLabel.Location = new System.Drawing.Point(24, 20);
            this.titleLabel.Name = "titleLabel";
            this.titleLabel.TabIndex = 0;
            this.titleLabel.Text = "商城 · 健康产品";
            //
            // searchBox
            //
            this.searchBox.Location = new System.Drawing.Point(24, 66);
            this.searchBox.Name = "searchBox";
            this.searchBox.Size = new System.Drawing.Size(260, 26);
            this.searchBox.TabIndex = 1;
            //
            // searchBtn
            //
            this.searchBtn.Location = new System.Drawing.Point(300, 64);
            this.searchBtn.Name = "searchBtn";
            this.searchBtn.Size = new System.Drawing.Size(80, 28);
            this.searchBtn.TabIndex = 2;
            this.searchBtn.Text = "搜索";
            this.searchBtn.UseVisualStyleBackColor = true;
            this.searchBtn.Click += new System.EventHandler(this.searchBtn_Click);
            //
            // productListView
            //
            this.productListView.Location = new System.Drawing.Point(24, 108);
            this.productListView.Name = "productListView";
            this.productListView.Size = new System.Drawing.Size(520, 300);
            this.productListView.TabIndex = 3;
            this.productListView.UseCompatibleStateImageBehavior = false;
            //
            // addCartBtn
            //
            this.addCartBtn.Location = new System.Drawing.Point(24, 424);
            this.addCartBtn.Name = "addCartBtn";
            this.addCartBtn.Size = new System.Drawing.Size(120, 34);
            this.addCartBtn.TabIndex = 4;
            this.addCartBtn.Text = "加入购物车";
            this.addCartBtn.UseVisualStyleBackColor = true;
            this.addCartBtn.Click += new System.EventHandler(this.addCartBtn_Click);
            //
            // viewCartBtn
            //
            this.viewCartBtn.Location = new System.Drawing.Point(160, 424);
            this.viewCartBtn.Name = "viewCartBtn";
            this.viewCartBtn.Size = new System.Drawing.Size(120, 34);
            this.viewCartBtn.TabIndex = 5;
            this.viewCartBtn.Text = "查看购物车";
            this.viewCartBtn.UseVisualStyleBackColor = true;
            this.viewCartBtn.Click += new System.EventHandler(this.viewCartBtn_Click);
            //
            // ShopForm
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(568, 480);
            this.Controls.Add(this.viewCartBtn);
            this.Controls.Add(this.addCartBtn);
            this.Controls.Add(this.productListView);
            this.Controls.Add(this.searchBtn);
            this.Controls.Add(this.searchBox);
            this.Controls.Add(this.titleLabel);
            this.Name = "ShopForm";
            this.Text = "商城";
            this.Load += new System.EventHandler(this.ShopForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.Label titleLabel;
        private System.Windows.Forms.TextBox searchBox;
        private System.Windows.Forms.Button searchBtn;
        private System.Windows.Forms.ListView productListView;
        private System.Windows.Forms.Button addCartBtn;
        private System.Windows.Forms.Button viewCartBtn;
    }
}
