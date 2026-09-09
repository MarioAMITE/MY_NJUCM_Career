using System;

namespace 非酒精性脂肪肝健康管理APP.Entities
{
    /// <summary>
    /// 患者日常行为日志：饮食 / 运动 / 用药 / 睡眠 / 体重。
    /// </summary>
    public class BehaviorLog
    {
        public long LogId { get; set; }

        public int ProfileId { get; set; }

        public DateTime LogDate { get; set; }

        /// <summary>类型：diet / exercise / medication / sleep / weight。</summary>
        public string LogType { get; set; }

        /// <summary>内容描述。</summary>
        public string Content { get; set; }

        /// <summary>热量（kcal）。</summary>
        public decimal Calories { get; set; }

        /// <summary>步数。</summary>
        public int Steps { get; set; }

        /// <summary>时长（分钟）。</summary>
        public int DurationMinutes { get; set; }

        /// <summary>用药依从性（如：按时 / 漏服 / 停药）。</summary>
        public string MedicationAdherence { get; set; }

        public string Remark { get; set; }
    }
}
