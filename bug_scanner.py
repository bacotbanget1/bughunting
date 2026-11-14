import sys
import requests
import json
from urllib.parse import quote
from bug_hunter import check_xss, check_sqli
from tools.api_token_checker import check_api_token
from tools.js_checker import check_js_xss

# Daftar parameter umum (sebagai fallback jika parameter.json tidak ada)
DEFAULT_PARAMETERS = ["id", "q", "page", "user"]
PARAMETER_FILE = "parameter.json"

def load_parameters_from_file():
    """Mencoba memuat daftar parameter dari parameter.json."""
    try:
        with open(PARAMETER_FILE, 'r') as f:
            data = json.load(f)
            if 'parameters' in data and isinstance(data['parameters'], list):
                print(f"[*] Berhasil memuat {len(data['parameters'])} parameter dari {PARAMETER_FILE}.")
                return data['parameters']
    except FileNotFoundError:
        print(f"[!] File {PARAMETER_FILE} tidak ditemukan. Menggunakan parameter default.")
    except json.JSONDecodeError:
        print(f"[!] Error parsing JSON di {PARAMETER_FILE}. Menggunakan parameter default.")
    except Exception as e:
        print(f"[!] Error saat memuat parameter: {e}. Menggunakan parameter default.")
        
    return DEFAULT_PARAMETERS

def run_all_scans(target_url, parameters):
    """Menjalankan semua jenis pengujian pada parameter yang diberikan."""
    print(f"--- Memulai Comprehensive Bug Hunting pada {target_url} ---")
    
    if not parameters:
        print("[!] Tidak ada parameter yang ditentukan dan tidak ditemukan di file. Menggunakan parameter default.")
        parameters = DEFAULT_PARAMETERS
    else:
        print(f"[*] Menguji {len(parameters)} parameter: {', '.join(parameters)}")
    
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
        print("Penggunaan: python bug_scanner.py <target_url> [param1] [param2] ...")
        print("Catatan: Jika tidak ada parameter, tool akan membaca dari parameter.json atau menggunakan default.")
        sys.exit(1)

    target_url = sys.argv[1]
    
    # Cek apakah ada argumen parameter tambahan di CLI
    cli_parameters = sys.argv[2:]
    
    if cli_parameters:
        parameters_to_scan = cli_parameters
        print(f"[*] Menggunakan parameter dari CLI: {', '.join(cli_parameters)}")
    else:
        # Jika tidak ada di CLI, coba muat dari file JSON
        parameters_to_scan = load_parameters_from_file()
    
    run_all_scans(target_url, parameters_to_scan)
    print("\n--- SEMUA PENGUJIAN SELESAI ---")