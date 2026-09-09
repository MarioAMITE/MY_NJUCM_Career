using System;

namespace 非酒精性脂肪肝健康管理APP.Entities
{
    /// <summary>智能饮食分析记录。</summary>
    public class AiAnalysisRecord
    {
        public long RecordId { get; set; }

        public int ProfileId { get; set; }

        /// <summary>饮食描述或图片路径。</summary>
        public string Input { get; set; }

        /// <summary>识别 / 分析结果。</summary>
        public string Result { get; set; }

        public DateTime AnalyzedAt { get; set; }
    }
}
