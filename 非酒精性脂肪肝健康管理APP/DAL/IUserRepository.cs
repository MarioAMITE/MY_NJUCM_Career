using System.Collections.Generic;
using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>用户数据访问接口（占位：待实现 SQL 访问）。</summary>
    public interface IUserRepository
    {
        User GetById(int userId);

        User GetByUsername(string username);

        List<User> GetAll();

        int Insert(User user);

        bool Update(User user);

        bool Delete(int userId);
    }
}
