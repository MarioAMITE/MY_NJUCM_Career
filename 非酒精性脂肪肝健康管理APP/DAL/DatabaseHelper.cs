using System.Configuration;
using MySql.Data.MySqlClient;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>
    /// MySQL 数据库连接助手。
    /// 连接字符串从 App.config 的 connectionStrings[NafldDb] 读取，缺省使用本地默认值。
    /// </summary>
    public static class DatabaseHelper
    {
        private const string DefaultConnectionString =
            "Server=localhost;Port=3306;Database=nafld_health;Uid=root;Pwd=123456;CharSet=utf8mb4;";

        /// <summary>获取数据库连接字符串。</summary>
        public static string ConnectionString
        {
            get
            {
                string cs = ConfigurationManager.ConnectionStrings["NafldDb"]?.ConnectionString;
                return string.IsNullOrEmpty(cs) ? DefaultConnectionString : cs;
            }
        }

        /// <summary>创建一个新的 MySQL 连接（未打开）。</summary>
        public static MySqlConnection GetConnection()
        {
            return new MySqlConnection(ConnectionString);
        }
    }
}
