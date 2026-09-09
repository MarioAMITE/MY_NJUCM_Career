using System.Collections.Generic;
using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>医患咨询消息数据访问接口（占位：待实现 SQL 访问）。</summary>
    public interface IConsultMessageRepository
    {
        List<ConsultMessage> GetBySession(int sessionId);

        long Insert(ConsultMessage message);

        bool MarkAsRead(long messageId);
    }
}
