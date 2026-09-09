using System;
using System.Collections.Generic;
using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>行为日志数据访问接口（占位：待实现 SQL 访问）。</summary>
    public interface IBehaviorLogRepository
    {
        BehaviorLog GetById(long logId);

        List<BehaviorLog> GetByProfile(int profileId);

        List<BehaviorLog> GetByProfileAndType(int profileId, string logType);

        List<BehaviorLog> GetByProfileAndDateRange(int profileId, DateTime start, DateTime end);

        long Insert(BehaviorLog log);

        bool Update(BehaviorLog log);

        bool Delete(long logId);
    }
}
