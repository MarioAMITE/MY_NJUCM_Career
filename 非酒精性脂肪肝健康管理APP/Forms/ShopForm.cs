using System;
using System.Windows.Forms;

namespace 非酒精性脂肪肝健康管理APP.Forms
{
    /// <summary>商城：健康产品浏览与购物。</summary>
    public partial class ShopForm : Form
    {
        public ShopForm()
        {
            InitializeComponent();
            InitProductList();
        }

        private void InitProductList()
        {
            productListView.View = View.Details;
            productListView.FullRowSelect = true;
            productListView.GridLines = true;
            productListView.Columns.Add("商品名称", 180);
            productListView.Columns.Add("分类", 120);
            productListView.Columns.Add("价格(元)", 80);
            productListView.Columns.Add("库存", 60);
        }

        private void ShopForm_Load(object sender, EventArgs e)
        {
            // TODO: 从 IProductRepository.GetAll() 加载商品到 productListView
        }

        private void searchBtn_Click(object sender, EventArgs e)
        {
            // TODO: 调用 IProductRepository.Search(searchBox.Text) 过滤列表
        }

        private void addCartBtn_Click(object sender, EventArgs e)
        {
            // TODO: 将选中商品加入购物车
        }

        private void viewCartBtn_Click(object sender, EventArgs e)
        {
            // TODO: 打开购物车视图
        }
    }
}
