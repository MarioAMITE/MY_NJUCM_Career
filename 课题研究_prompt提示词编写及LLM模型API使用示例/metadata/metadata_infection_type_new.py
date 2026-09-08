#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Map Infection_type from bio_project_info input.
Usage:
  python3 metadata_infection_type_new.py /path/to/bio_info.txt
Or:
  python3 metadata_infection_type_new.py /data2/boyi/wangkai/metadata_combined/bio_project_info.txt
Output:
  /data2/boyi/wangkai/metadata_combined/metadata_infection_type.txt
"""
import os
import sys
import argparse
import pandas as pd
import re

OUT_DIR = "/data2/boyi/wangkai/metadata_combined"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "metadata_infection_type.txt")

def map_infection_type(icd, major, minor):
    if pd.isna(icd): icd = ""
    icd = str(icd).upper().strip()
    major = str(major).lower() if major is not None else ""
    minor = str(minor).lower() if minor is not None else ""

    # ICD based rules
    if re.match(r"^1A|^1B|^1C", icd):
        return "Bacterial_Extracellular"
    elif re.match(r"^1D|^1E", icd):
        return "Viral_RNA"
    elif re.match(r"^1F2|^1F5|^1F8", icd):
        return "Fungal_Yeast"
    elif re.match(r"^1F4|^1F6", icd):
        return "Parasitic_Protozoa"
    elif re.match(r"^1G", icd):
        return "Host_response"
    elif re.match(r"^2", icd):
        return "Neoplasm"
    elif re.match(r"^4", icd):
        return "Autoimmune"
    elif re.match(r"^5|^6|^7|^8|^9|^Q|^N", icd):
        return "Other_noninfectious"

    # Keyword fallback - use minor first, then major
    text = minor + " " + major

    # Viral RNA
    if any(k in text for k in ["covid", "influenza", "hiv", "dengue", "zika", "ebola", "rsv", "sars-cov", "measles", "mumps", "coronavirus"]):
        return "Viral_RNA"
    # Viral DNA
    if any(k in text for k in ["hbv", "hcv", "herpes", "cmv", "ebv", "adenovirus", "papilloma", "pox", "varicella", "parvovirus"]):
        return "Viral_DNA"
    # Bacterial intracellular
    if any(k in text for k in ["mycobacterium", "tuberculosis", "chlamydia", "rickettsia", "brucella", "legionella", "listeria", "salmonella", "yersinia"]):
        return "Bacterial_Intracellular"
    # Bacterial extracellular
    if any(k in text for k in ["staphylococcus", "streptococcus", "pseudomonas", "vibrio", "enterococcus", "neisseria", "bacillus", "clostridium", "escherichia"]):
        return "Bacterial_Extracellular"
    # Fungal yeast
    if any(k in text for k in ["candida", "cryptococcus"]):
        return "Fungal_Yeast"
    # Fungal mold
    if any(k in text for k in ["aspergillus", "mucor", "histoplasma", "blastomyces", "coccidioides"]):
        return "Fungal_Mold"
    # Parasitic protozoa
    if any(k in text for k in ["plasmodium", "malaria", "leishmania", "trypanosoma", "giardia", "toxoplasma"]):
        return "Parasitic_Protozoa"
    # Parasitic helminth
    if any(k in text for k in ["schistosoma", "ascaris", "trichuris", "taenia", "echinococcus", "filaria", "strongyloides"]):
        return "Parasitic_Helminth"
    # Mixed
    if "mixed" in text or "co-infection" in text or "co infection" in text:
        return "Mixed"
    # Host response
    if any(k in text for k in ["sepsis", "shock", "sirs", "cytokine", "cytokine storm"]):
        return "Host_response"
    # Autoimmune
    if any(k in text for k in ["arthritis", "lupus", "autoimmune", "ibd", "psoriasis", "inflammatory", "celiac", "sclerosis"]):
        return "Autoimmune"
    # Neoplasm
    if any(k in text for k in ["cancer", "tumor", "carcinoma", "leukemia", "sarcoma", "glioblastoma", "astrocytoma", "meningioma"]):
        return "Neoplasm"
    # Control
    if any(k in text for k in ["control", "healthy", "uninfected"]):
        return "Control"

    return "Other_noninfectious"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("bio_info_path", help="Path to bio_project_info.txt (pipe-separated)")
    args = p.parse_args()
    bio_path = args.bio_info_path
    if not os.path.exists(bio_path):
        print(f"ERROR: input file not found: {bio_path}", file=sys.stderr)
        sys.exit(2)

    df = pd.read_csv(bio_path, sep="|", dtype=str, keep_default_na=False)
    df["Infection_type"] = df.apply(lambda r: map_infection_type(r.get("icd11_code",""), r.get("disease_major",""), r.get("disease_minor","")), axis=1)
    df.to_csv(OUT_PATH, sep="|", index=False)
    print(f"? Infection type classification completed.\nOutput saved to: {OUT_PATH}")

if __name__ == "__main__":
    main()
