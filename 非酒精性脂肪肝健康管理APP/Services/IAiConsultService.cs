using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.Services
{
    /// <summary>
    /// 智能健康咨询接口（占位：待实现）。
    /// 根据患者档案生成个性化健康建议。
    /// </summary>
    public interface IAiConsultService
    {
        /// <summary>根据患者档案生成个性化健康建议。</summary>
        string GenerateAdvice(PatientProfile profile);
    }
}
