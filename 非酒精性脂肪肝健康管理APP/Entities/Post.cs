using System;

namespace 非酒精性脂肪肝健康管理APP.Entities
{
    /// <summary>论坛帖子。</summary>
    public class Post
    {
        public int PostId { get; set; }

        public int UserId { get; set; }

        /// <summary>板块（如：饮食经验 / 运动打卡 / 用药交流）。</summary>
        public string Board { get; set; }

        public string Title { get; set; }

        public string Content { get; set; }

        public DateTime CreatedAt { get; set; }
    }

    /// <summary>论坛回帖。</summary>
    public class Reply
    {
        public int ReplyId { get; set; }

        public int PostId { get; set; }

        public int UserId { get; set; }

        public string Content { get; set; }

        public DateTime CreatedAt { get; set; }
    }
}
