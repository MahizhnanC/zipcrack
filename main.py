import zipfile
import argparse
from tqdm import tqdm
import os
import sys

def crack_zip(file_path, digits):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        zip_file = zipfile.ZipFile(file_path)
    except zipfile.BadZipFile:
        print("❌ Not a valid ZIP file.")
        return

    total = 10 ** digits
    print(f"🔍 Brute-forcing ZIP: {file_path}")
    print(f"🔢 Trying {total:,} combinations (numeric, {digits} digits)...")

    try:
        for i in tqdm(range(total), desc="Trying passwords", ncols=80):
            password = str(i).zfill(digits).encode('utf-8')
            try:
                zip_file.extractall(pwd=password)
                print(f"\n✅ Password found: {password.decode()}")
                return
            except RuntimeError as e:
                if 'Bad password' in str(e):
                    continue
                else:
                    print(f"⚠️ Unexpected error: {e}")
                    continue
            except Exception as e:
                continue
    except KeyboardInterrupt:
        print("\n🛑 Brute-force interrupted by user.")
        sys.exit(0)

    print("❌ Password not found.")

def main():
    try:
        parser = argparse.ArgumentParser(description="Brute-force numeric ZIP file passwords")
        parser.add_argument("--file", "-f", required=True, help="Path to the password-protected ZIP file")
        parser.add_argument("--digits", "-d", type=int, default=9, help="Number of digits in the password (default: 9)")

        args = parser.parse_args()
        crack_zip(args.file, args.digits)

    except KeyboardInterrupt:
        print("\n🛑 Interrupted before start.")
        sys.exit(0)
