using System;

namespace 非酒精性脂肪肝健康管理APP.Entities
{
    /// <summary>健康商城商品。</summary>
    public class Product
    {
        public int ProductId { get; set; }

        public string Name { get; set; }

        /// <summary>分类（如：低脂食品 / 营养补充剂 / 健康监测设备）。</summary>
        public string Category { get; set; }

        public decimal Price { get; set; }

        public int Stock { get; set; }

        public string Description { get; set; }

        public string ImageUrl { get; set; }
    }
}
