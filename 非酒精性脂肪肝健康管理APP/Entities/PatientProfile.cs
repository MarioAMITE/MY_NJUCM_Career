using System;

namespace 非酒精性脂肪肝健康管理APP.Entities
{
    /// <summary>
    /// 患者电子档案（脱敏）。
    /// 覆盖生化指标、体格指标等 20 余项特征。
    /// </summary>
    public class PatientProfile
    {
        public int ProfileId { get; set; }

        public int UserId { get; set; }

        public string RealName { get; set; }

        /// <summary>性别。</summary>
        public string Gender { get; set; }

        public DateTime BirthDate { get; set; }

        /// <summary>身高（cm）。</summary>
        public decimal Height { get; set; }

        /// <summary>体重（kg）。</summary>
        public decimal Weight { get; set; }

        /// <summary>体质指数 BMI。</summary>
        public decimal Bmi { get; set; }

        /// <summary>腰围（cm）。</summary>
        public decimal Waistline { get; set; }

        // ---- 生化指标 ----

        /// <summary>谷丙转氨酶 ALT（U/L）。</summary>
        public decimal Alt { get; set; }

        /// <summary>谷草转氨酶 AST（U/L）。</summary>
        public decimal Ast { get; set; }

        /// <summary>γ-谷氨酰转肽酶 GGT（U/L）。</summary>
        public decimal Ggt { get; set; }

        /// <summary>总胆固醇 TC（mmol/L）。</summary>
        public decimal TotalCholesterol { get; set; }

        /// <summary>甘油三酯 TG（mmol/L）。</summary>
        public decimal Triglyceride { get; set; }

        /// <summary>高密度脂蛋白 HDL（mmol/L）。</summary>
        public decimal Hdl { get; set; }

        /// <summary>低密度脂蛋白 LDL（mmol/L）。</summary>
        public decimal Ldl { get; set; }

        /// <summary>空腹血糖 FBG（mmol/L）。</summary>
        public decimal FastingGlucose { get; set; }

        /// <summary>尿酸 UA（μmol/L）。</summary>
        public decimal UricAcid { get; set; }

        /// <summary>糖化血红蛋白 HbA1c（%）。</summary>
        public decimal Hba1c { get; set; }

        /// <summary>肝脂肪含量（%）。</summary>
        public decimal LiverFatContent { get; set; }

        /// <summary>收缩压（mmHg）。</summary>
        public int BloodPressureSystolic { get; set; }

        /// <summary>舒张压（mmHg）。</summary>
        public int BloodPressureDiastolic { get; set; }

        /// <summary>肝纤维化分期（如 F0-F4）。</summary>
        public string FibrosisStage { get; set; }

        public DateTime DiagnosisDate { get; set; }

        public string Note { get; set; }
    }
}
