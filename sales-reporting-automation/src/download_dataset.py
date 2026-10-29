"""
Dataset Downloader & Extractor
Source: UCI Machine Learning Repository — Online Retail
URL: https://archive.ics.uci.edu/dataset/352/online+retail
"""

import sys
import zipfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

UCI_URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
ZIP_PATH = RAW_DIR / "online_retail.zip"
TARGET_FILE = RAW_DIR / "Online Retail.xlsx"

def download_and_extract():
    if TARGET_FILE.exists():
        size_mb = TARGET_FILE.stat().st_size / (1024 * 1024)
        print(f"[OK] Dataset already present: {TARGET_FILE.name} ({size_mb:.2f} MB)")
        return

    print("=" * 65)
    print("DOWNLOADING UCI ONLINE RETAIL DATASET")
    print(f"Target: {UCI_URL}")
    print("=" * 65)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(UCI_URL, headers=headers)

    print("Connecting to UCI Machine Learning Repository...")
    with urllib.request.urlopen(req, timeout=60) as response, open(ZIP_PATH, "wb") as out_file:
        chunk_size = 1024 * 64
        downloaded = 0
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
            downloaded += len(chunk)
            mb = downloaded / (1024 * 1024)
            sys.stdout.write(f"\rDownloaded: {mb:.2f} MB")
            sys.stdout.flush()

    print(f"\n[OK] Download completed: {ZIP_PATH.name} ({ZIP_PATH.stat().st_size / (1024 * 1024):.2f} MB)")

    print("Extracting archive...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(RAW_DIR)

    # Check extracted contents
    extracted_files = list(RAW_DIR.glob("*.xlsx")) + list(RAW_DIR.glob("*.csv"))
    print("[OK] Extracted files in data/raw/:")
    for f in extracted_files:
        print(f"  - {f.name} ({f.stat().st_size / (1024 * 1024):.2f} MB)")

    # Clean up zip archive if extraction was successful
    if TARGET_FILE.exists():
        ZIP_PATH.unlink(missing_ok=True)
        print(f"[OK] Ready for processing: {TARGET_FILE}")
    else:
        print("[NOTE] Extracted files did not include 'Online Retail.xlsx' directly. Check filenames above.")

if __name__ == "__main__":
    download_and_extract()
