namespace 非酒精性脂肪肝健康管理APP.Services
{
    /// <summary>
    /// 饮食图像识别接口（占位）。
    /// 预留：可接入 ML 模型或第三方图像识别 API，返回识别出的食物名称。
    /// </summary>
    public interface IDietImageRecognizer
    {
        /// <summary>识别图片中的食物，返回食物名称（未实现）。</summary>
        string Recognize(string imagePath);
    }
}
