import sys
import requests
from urllib.parse import quote
from bug_hunter import check_xss, check_sqli
from tools.api_token_checker import check_api_token
from tools.js_checker import check_js_xss

def run_all_scans(target_url, parameters):
    """Menjalankan semua jenis pengujian pada parameter yang diberikan."""
    print(f"--- Memulai Comprehensive Bug Hunting pada {target_url} ---")
    
    for param in parameters:
        print(f"\n=====================================================")
        print(f"[*] MENGUJI PARAMETER: {param}")
        print(f"=====================================================")
        
        # 1. XSS Check
        check_xss(target_url, param)
        
        # 2. SQLi Check
        check_sqli(target_url, param)
        
        # 3. API Token/Key Check
        check_api_token(target_url, param)
        
        # 4. JavaScript/DOM XSS Check
        check_js_xss(target_url, param)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan: python bug_scanner.py <target_url> <param1> [param2] ...")
        print("Contoh: python bug_scanner.py http://target.com/page id user_input")
        sys.exit(1)

    target_url = sys.argv[1]
    # Ambil semua argumen setelah URL sebagai daftar parameter
    parameters = sys.argv[2:]
    
    run_all_scans(target_url, parameters)
    print("\n--- SEMUA PENGUJIAN SELESAI ---")