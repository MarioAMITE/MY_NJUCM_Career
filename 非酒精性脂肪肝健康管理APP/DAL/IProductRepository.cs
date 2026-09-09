using System.Collections.Generic;
using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>商品数据访问接口（占位：待实现 SQL 访问）。</summary>
    public interface IProductRepository
    {
        Product GetById(int productId);

        List<Product> GetAll();

        List<Product> Search(string keyword);

        int Insert(Product product);

        bool Update(Product product);

        bool Delete(int productId);
    }
}
