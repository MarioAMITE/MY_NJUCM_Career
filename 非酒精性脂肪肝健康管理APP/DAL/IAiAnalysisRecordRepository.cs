using System.Collections.Generic;
using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>饮食分析记录数据访问接口（占位：待实现 SQL 访问）。</summary>
    public interface IAiAnalysisRecordRepository
    {
        List<AiAnalysisRecord> GetByProfile(int profileId);

        long Insert(AiAnalysisRecord record);
    }
}
