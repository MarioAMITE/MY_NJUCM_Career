namespace 非酒精性脂肪肝健康管理APP.Services
{
    /// <summary>
    /// 运动监测服务接口（占位：待实现）。
    /// 融合步数、运动类型等数据，输出运动量汇总与达标情况。
    /// </summary>
    public interface IMotionMonitorService
    {
        /// <summary>汇总运动数据（步数、运动类型），返回达标情况说明。</summary>
        string Summarize(int steps, string activityType);
    }
}
