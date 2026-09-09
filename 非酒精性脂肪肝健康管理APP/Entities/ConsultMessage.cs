using System;

namespace 非酒精性脂肪肝健康管理APP.Entities
{
    /// <summary>医患咨询消息。</summary>
    public class ConsultMessage
    {
        public long MessageId { get; set; }

        /// <summary>会话编号。</summary>
        public int SessionId { get; set; }

        /// <summary>发送方用户编号（患者或医生）。</summary>
        public int SenderId { get; set; }

        /// <summary>接收方用户编号。</summary>
        public int ReceiverId { get; set; }

        public string Content { get; set; }

        public DateTime SentAt { get; set; }

        public bool IsRead { get; set; }
    }
}
