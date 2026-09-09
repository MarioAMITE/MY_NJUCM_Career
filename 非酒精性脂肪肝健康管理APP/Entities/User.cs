using System;

namespace 非酒精性脂肪肝健康管理APP.Entities
{
    /// <summary>用户（患者 / 医生 / 管理员）。</summary>
    public class User
    {
        public int UserId { get; set; }

        public string Username { get; set; }

        public string PasswordHash { get; set; }

        /// <summary>角色：patient / doctor / admin。</summary>
        public string Role { get; set; }

        public string RealName { get; set; }

        public string Phone { get; set; }

        public DateTime CreatedAt { get; set; }
    }
}
