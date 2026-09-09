using System.Collections.Generic;
using 非酒精性脂肪肝健康管理APP.Entities;

namespace 非酒精性脂肪肝健康管理APP.DAL
{
    /// <summary>患者电子档案数据访问接口（占位：待实现 SQL 访问）。</summary>
    public interface IPatientRepository
    {
        PatientProfile GetById(int profileId);

        PatientProfile GetByUserId(int userId);

        List<PatientProfile> GetAll();

        int Insert(PatientProfile profile);

        bool Update(PatientProfile profile);

        bool Delete(int profileId);
    }
}
