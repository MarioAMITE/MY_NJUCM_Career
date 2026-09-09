using System.Collections.Generic;
using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>论坛帖子/回帖数据访问接口（占位：待实现 SQL 访问）。</summary>
    public interface IPostRepository
    {
        Post GetPostById(int postId);

        List<Post> GetPostsByBoard(string board);

        List<Reply> GetReplies(int postId);

        int InsertPost(Post post);

        int InsertReply(Reply reply);
    }
}
