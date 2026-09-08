#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import subprocess
import pandas as pd
from pathlib import Path

OUT_DIR = "/data2/boyi/wangkai/metadata_combined"
os.makedirs(OUT_DIR, exist_ok=True)
BIO_INFO = os.path.join(OUT_DIR, "bio_project_info.txt")
INFECT = os.path.join(OUT_DIR, "metadata_infection_type.txt")
GROUPING = os.path.join(OUT_DIR, "grouping_results.txt")
FINAL = os.path.join(OUT_DIR, "combined_metadata_summary.txt")

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
# assume new scripts are in same folder as this master script
PARSE_BIO_PYTHON = "/home/yuanshaoxun/miniconda3/envs/YSXconda/bin/python"
PARSE_BIO_FILE = "/data2/boyi/wangkai/code/parse_bioproject.py"

BIO_SCRIPT = os.path.join(THIS_DIR, "bio_project_info_new.py")
INF_SCRIPT = os.path.join(THIS_DIR, "metadata_infection_type_new.py")
PARSE_SCRIPT = os.path.join(THIS_DIR, "parse_metadata_summary_new.py")
PARSE_BP_SCRIPT = "/data2/boyi/wangkai/code/parse_bioproject.py"

def run_cmd(cmd):
    print(">>> Running:", " ".join(cmd))
    r = subprocess.run(cmd, check=False)
    if r.returncode != 0:
        print("WARNING: command returned non-zero:", r.returncode)

def merge_and_write():
    if not os.path.exists(BIO_INFO):
        print("ERROR: missing bio info file:", BIO_INFO)
        return
    bio_df = pd.read_csv(BIO_INFO, sep="|", dtype=str, keep_default_na=False)

    if os.path.exists(INFECT):
        inf_df = pd.read_csv(INFECT, sep="|", dtype=str, keep_default_na=False)
    else:
        inf_df = None

    grouping_map = {}
    if os.path.exists(GROUPING):
        with open(GROUPING, "r", encoding="utf-8") as fr:
            for ln in fr:
                ln = ln.rstrip("\n")
                if not ln: continue
                parts = ln.split(",", 1)
                prj = parts[0]
                rest = parts[1] if len(parts) > 1 else ""
                m = []
                i = 0
                current = ""
                in_quote = False
                while i < len(rest):
                    ch = rest[i]
                    if ch == '"' and (i==0 or rest[i-1] != "\\"):
                        in_quote = not in_quote
                        current += ch
                    elif ch == ',' and not in_quote:
                        m.append(current.strip())
                        current = ""
                    else:
                        current += ch
                    i += 1
                if current:
                    m.append(current.strip())
                if len(m) >= 3:
                    grouping = m[0].strip().strip('"')
                    group_info = m[1].strip().strip('"')
                    group_count = m[2].strip().strip('"')
                else:
                    grouping = ""
                    group_info = ""
                    group_count = ""
                grouping_map[prj] = {"grouping": grouping, "group_info": group_info, "group_count": group_count}

    rows = []
    for _, r in bio_df.iterrows():
        prj = r.get("bio_project", "")
        infection_type = ""
        if inf_df is not None and "bio_project" in inf_df.columns:
            sub = inf_df[inf_df["bio_project"] == prj]
            if len(sub) > 0:
                infection_type = sub.iloc[0].get("Infection_type", "")
        grp = grouping_map.get(prj, {"grouping":"", "group_info":"", "group_count":""})
        row = {
            "BioProject": prj,
            "GEO_Accession": r.get("geo_accession",""),
            "pubmed_id": r.get("pmid",""),
            "journal_name": r.get("journal_name",""),
            "publication_data": r.get("publication_data",""),
            "publication_doi": r.get("publication_doi",""),
            "species": r.get("species",""),
            "disease_major": r.get("disease_major",""),
            "disease_minor": r.get("disease_minor",""),
            "icd11_code": r.get("icd11_code",""),
            "Infection_type": infection_type,
            "sample_source": r.get("sample_source",""),
            "instrument": r.get("instrument",""),
            "library_strategy": r.get("library_strategy",""),
            "library_source": r.get("library_source",""),
            "library_selection": r.get("library_selection",""),
            "library_layout": r.get("library_layout",""),
            "sample_size": r.get("sample_size",""),
            "grouping": grp.get("grouping",""),
            "group_info": grp.get("group_info",""),
            "group_count": grp.get("group_count","")
        }
        rows.append(row)

    final_df = pd.DataFrame(rows, columns=[
        "BioProject","GEO_Accession","pubmed_id","journal_name","publication_data","publication_doi",
        "species","disease_major","disease_minor","icd11_code","Infection_type","sample_source",
        "instrument","library_strategy","library_source","library_selection","library_layout",
        "sample_size","grouping","group_info","group_count"
    ])
    final_df = final_df.fillna("")

    # 判断文件是否存在，如果存在则追加且不写 header
    if not os.path.exists(FINAL):
        final_df.to_csv(FINAL, sep="|", index=False)
    else:
        final_df.to_csv(FINAL, sep="|", index=False, mode='a', header=False)

    print(f"\nDone. Final combined file: {FINAL}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("metadata_dir", help="Directory with metadata Excel files")
    p.add_argument("prjna", help="Single PRJNA or path to PRJNA list")
    args = p.parse_args()

    # ==== 新增：先调用 parse_bioproject.py ====
    prjna_list = []
    if os.path.isfile(args.prjna):
        with open(args.prjna) as fr:
            prjna_list = [line.strip() for line in fr if line.strip()]
    else:
        prjna_list = [args.prjna.strip()]

    for prj in prjna_list:
        print(f">>> Generating {prj}_metadata.xlsx via parse_bioproject alias ...")
        subprocess.run([
            "bash",
            "-i",
            "-c",
            f"parse_bioproject {prj} --outdir {args.metadata_dir}"
        ], check=True)

    # ==== 调用 bio_project_info_new.py ====
    run_cmd(["python3", BIO_SCRIPT, args.metadata_dir, args.prjna])

    # run metadata_infection_type_new.py using produced bio file
    run_cmd(["python3", INF_SCRIPT, BIO_INFO])

    # run parse_metadata_summary_new.py
    run_cmd(["python3", PARSE_SCRIPT, args.metadata_dir, args.prjna])

    # merge and write final
    merge_and_write()

if __name__ == "__main__":
    main()

