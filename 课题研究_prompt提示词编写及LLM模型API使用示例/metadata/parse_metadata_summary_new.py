#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process grouping rules and metadata to build compact grouping lines.

Usage:
    python3 parse_metadata_summary_new.py /path/to/metadata_dir PRJNAxxxx
    python3 parse_metadata_summary_new.py /path/to/metadata_dir /path/to/prjna_list.txt

Output:
    /data2/boyi/wangkai/metadata_combined/grouping_results.txt

Notes:
    DeepSeek integration retained; use env var DEEPSEEK_API_KEY to enable.
"""

import os
import sys
import argparse
import json
import time
import re
import pandas as pd
import requests

# --------------------------------------------------------------------
# Output folder
# --------------------------------------------------------------------
OUT_DIR = "/data2/boyi/wangkai/metadata_combined"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "grouping_results.txt")

# --------------------------------------------------------------------
# DeepSeek config
# --------------------------------------------------------------------
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL_NAME = "deepseek-chat"
TIMEOUT = 120


# --------------------------------------------------------------------
# Utility: parse PRJNA arguments
# --------------------------------------------------------------------
def parse_prjna_arg(arg):
    if os.path.exists(arg) and os.path.isfile(arg):
        with open(arg, "r", encoding="utf-8") as fr:
            prs = [ln.strip() for ln in fr if ln.strip()]
        return set(prs)
    else:
        return {arg.strip()}


# --------------------------------------------------------------------
# Utility: clean labels
# --------------------------------------------------------------------
def clean_label(lbl: str) -> str:
    if not isinstance(lbl, str):
        lbl = str(lbl)
    s = lbl.strip()
    s = re.sub(r'GSM\\d+\\s*:\\s*', '', s, flags=re.IGNORECASE)
    if ';' in s:
        s = s.split(';', 1)[0]
    s = re.sub(r'\\s*\\(.*?\\)\\s*$', '', s)
    s = s.replace(',', ' ')
    s = re.sub(r'\\s+', ' ', s).strip()
    return s if s else "/"


# --------------------------------------------------------------------
# Build compact line (pre-counted)
# --------------------------------------------------------------------
def build_compact_line(prjna: str, group_cols: list, meta_df: pd.DataFrame):
    names, values_list, counts_list = [], [], []

    for col in group_cols:
        names.append(col)
        vc = meta_df[col].fillna("").astype(str)

        seen, ordered = {}, []
        for v in vc:
            k = v.strip()
            if k == "":
                continue
            if k not in seen:
                seen[k] = 0
                ordered.append(k)
            seen[k] += 1

        cleaned = [clean_label(x) for x in ordered]
        counts = [str(seen[x]) for x in ordered]

        values_list.append("|".join(cleaned) if cleaned else "/")
        counts_list.append("|".join(counts) if counts else "/")

    grouping_str = ", ".join(names)
    bracketed_values = ",".join(f"[{v}]" for v in values_list)
    bracketed_counts = ",".join(f"[{c}]" for c in counts_list)

    compact = f'{prjna},"{grouping_str}","{bracketed_values}","{bracketed_counts}"'
    return compact


# --------------------------------------------------------------------
# Load mapping rules
# --------------------------------------------------------------------
def load_mapping_rules(rules_df: pd.DataFrame):
    mapping = {}
    for _, row in rules_df.iterrows():
        colname = str(row.get("column_name", "")).strip()
        logic = row.get("grouping_logic", "")
        if not colname:
            continue

        if isinstance(logic, str) and logic.strip():
            try:
                parsed = json.loads(logic)
                mapping[colname] = parsed
            except Exception:
                try:
                    parsed = eval(logic)
                    if isinstance(parsed, dict):
                        mapping[colname] = parsed
                except Exception:
                    mapping[colname] = {}
        else:
            mapping[colname] = {}
    return mapping


# --------------------------------------------------------------------
# Build DeepSeek prompt
# --------------------------------------------------------------------
def build_strict_prompt(compact_line: str, mapping_rules: dict):
    prompt = f"""
You are given pre-counted RNA-seq grouping metadata in a structured CSV-like format.
DO NOT change counts. Your job is to standardize group names and remove redundant dimensions.

Input format:
PRJNAxxxx,"grouping_variables","[labels_group1],[labels_group2],...","[counts_group1],[counts_group2],..."

Instructions:
1. Keep the four-column structure exactly.
2. Never alter counts.
3. Remove meaningless or redundant grouping dimensions.
4. Retain only biologically meaningful variables.
5. Merge duplicate labels.
6. Output only the cleaned line.

Process this input:
{compact_line}
"""
    return prompt


# --------------------------------------------------------------------
# Call DeepSeek
# --------------------------------------------------------------------
def call_deepseek(prompt: str):
    if not DEEPSEEK_API_KEY:
        return None

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a strict structured-data transformer."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.0
    }

    try:
        r = requests.post(API_URL, headers=headers, json=payload, timeout=TIMEOUT)
        r.raise_for_status()
        j = r.json()

        content = j["choices"][0]["message"]["content"].strip()
        for line in content.splitlines():
            if line.strip().upper().startswith("PRJNA"):
                return line.strip()
        return content.splitlines()[0].strip() if content else None
    except Exception:
        return None


# --------------------------------------------------------------------
# Process a single metadata file
# --------------------------------------------------------------------
def process_single_file(path, prjna):
    try:
        rules_df = pd.read_excel(path, sheet_name="grouping_rules")
    except Exception:
        rules_df = None

    try:
        meta_df = pd.read_excel(path, sheet_name="metadata")
    except Exception:
        meta_df = None

    # Normal processing path
    if rules_df is not None and meta_df is not None:
        if "column_name" in rules_df.columns:
            cols = [str(x).strip() for x in rules_df["column_name"].dropna().astype(str).tolist()]
            filtered_cols = []

            for c in cols:
                if c not in meta_df.columns:
                    continue
                if "experiment_title" in c.lower():
                    uniq = meta_df[c].nunique()
                    avg_len = meta_df[c].astype(str).map(len).mean()
                    if uniq > 20 or avg_len > 30:
                        continue
                filtered_cols.append(c)

            if not filtered_cols:
                return None, "no-valid-columns"

            compact = build_compact_line(prjna, filtered_cols, meta_df)
            mapping_rules = load_mapping_rules(rules_df)
            prompt = build_strict_prompt(compact, mapping_rules)
            mapped = call_deepseek(prompt)

            if mapped:
                return mapped, "mapped"
            else:
                return compact, "fallback-mapped"

    # Fallback: use experiment_title only
    if meta_df is not None and "experiment_title" in meta_df.columns:
        counts = meta_df["experiment_title"].fillna("").astype(str)
        seen, ordered = {}, []
        for v in counts:
            k = v.strip()
            if k == "":
                continue
            if k not in seen:
                seen[k] = 0
                ordered.append(k)
            seen[k] += 1

        cleaned = [clean_label(x) for x in ordered]
        cnts = [str(seen[x]) for x in ordered]
        grouping_str = "experiment_title"

        compact = f'{prjna},"{grouping_str}","[{"|".join(cleaned)}]","[{"|".join(cnts)}]"'
        return compact, "fallback-experiment"

    return None, "no-info"


# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser()
    p.add_argument("metadata_dir", help="Directory containing metadata Excel files")
    p.add_argument("prjna", help="Single PRJNA or path to PRJNA list file")
    args = p.parse_args()

    meta_dir = args.metadata_dir
    target_set = parse_prjna_arg(args.prjna)

    if not os.path.isdir(meta_dir):
        print(f"ERROR: metadata_dir not found: {meta_dir}", file=sys.stderr)
        sys.exit(2)

    files = sorted([f for f in os.listdir(meta_dir) if f.endswith("_metadata.xlsx")])

    results = []
    processed = set()
    fallback_mapped = []

    for fname in files:
        prjna = fname.replace("_metadata.xlsx", "")
        if prjna not in target_set:
            continue

        path = os.path.join(meta_dir, fname)
        out_line, status = process_single_file(path, prjna)

        if out_line:
            results.append(out_line)
            processed.add(prjna)
            if "fallback" in status:
                fallback_mapped.append(prjna)

        time.sleep(0.2)

    with open(OUT_PATH, "w", encoding="utf-8") as fw:
        for line in results:
            fw.write(line + "\n")

    print(f"Saved grouping results to: {OUT_PATH}")

    missing = [p for p in target_set if p not in processed]
    if missing:
        print("\nMissing PRJNA files:")
        for m in missing:
            print(" -", m)

    if fallback_mapped:
        print("\nFallback-mapped PRJNA:")
        for f in fallback_mapped:
            print(" -", f)


if __name__ == "__main__":
    main()

