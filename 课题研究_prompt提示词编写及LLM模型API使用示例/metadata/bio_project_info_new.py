#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract bioproject-level info from metadata Excel files.
Usage:
  python3 bio_project_info_new.py /path/to/metadata_dir PRJNAxxxx
  python3 bio_project_info_new.py /path/to/metadata_dir /path/to/prjna_list.txt
Output:
  /data2/boyi/wangkai/metadata_combined/bio_project_info.txt (pipe-separated)
"""
import os
import sys
import argparse
import pandas as pd

OUT_DIR = "/data2/boyi/wangkai/metadata_combined"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "bio_project_info.txt")

FIELDS = [
    "geo_accession", "pmid", "journal_name", "publication_data", "publication_doi",
    "species", "disease_major", "disease_minor", "icd11_code", "sample_source",
    "instrument", "library_strategy", "library_source", "library_selection",
    "library_layout", "sample_size"
]

HEADER = ["bio_project"] + FIELDS

def parse_prjna_arg(arg):
    # if arg path exists and is file -> read list, else treat arg as single PRJNA
    if os.path.exists(arg) and os.path.isfile(arg):
        with open(arg, "r", encoding="utf-8") as fr:
            prs = [ln.strip() for ln in fr if ln.strip()]
        return set(prs)
    else:
        return {arg.strip()}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("metadata_dir", help="Directory containing PRJNAxxx_metadata.xlsx files")
    p.add_argument("prjna", help="Single PRJNA (e.g. PRJNA12345) or path to txt list")
    args = p.parse_args()

    meta_dir = args.metadata_dir
    target_set = parse_prjna_arg(args.prjna)

    results = []
    if not os.path.isdir(meta_dir):
        print(f"ERROR: metadata_dir not found: {meta_dir}", file=sys.stderr)
        sys.exit(2)

    files = sorted([f for f in os.listdir(meta_dir) if f.endswith("_metadata.xlsx")])
    for fname in files:
        prjna = fname.replace("_metadata.xlsx", "")
        if prjna not in target_set:
            continue
        path = os.path.join(meta_dir, fname)
        try:
            df = pd.read_excel(path, sheet_name="bioproject", header=None)
        except Exception as e:
            print(f"? Failed to read {fname}: {e}", file=sys.stderr)
            continue
        df.columns = ["field", "value"]
        record = {"bio_project": prjna}
        for field in FIELDS:
            match = df[df["field"].str.lower() == field.lower()]
            record[field] = match["value"].iloc[0] if not match.empty else ""
        results.append(record)

    out_df = pd.DataFrame(results, columns=HEADER)
    out_df.to_csv(OUT_PATH, sep="|", index=False)
    print(f"? Results saved to {OUT_PATH}")

if __name__ == "__main__":
    main()
