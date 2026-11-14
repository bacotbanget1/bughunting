import requests
from tools.payloads import TOKEN_CHECK_PAYLOADS

def check_api_token(url, param):
    """Mencoba injeksi API Key atau Token."""
    print(f"[*] Menguji API Key/Token pada parameter: {param}")
    
    for payload in TOKEN_CHECK_PAYLOADS:
        # Asumsi parameter yang diuji adalah tempat token/key dimasukkan
        full_url = f"{url}?{param}={requests.utils.quote(payload)}"
        
        try:
            response = requests.get(full_url, timeout=10)
            
            # Logika deteksi: Jika respons 200 OK dan mengandung kata kunci sensitif (misal: 'admin', 'secret')
            # ATAU jika respons tidak mengembalikan error otorisasi (401/403)
            if response.status_code == 200 and ("admin" in response.text.lower() or "secret" in response.text.lower()):
                print("=====================================================")
                print(f"[!!!] BUG DITEMUKAN: Potensi API Key/Token Leak")
                print(f"    URL: {full_url}")
                print(f"    Parameter: {param}")
                print(f"    Severity: Critical")
                print("    Cara Uji: Kirim payload token/key dan periksa respons.")
                print("    Lokasi: URL parameter.")
                print("=====================================================")
                return True
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Error saat request: {e}")
            return False
    
    print("[+] Pengujian API Key/Token tidak terdeteksi pada percobaan ini.")
    return False

if __name__ == '__main__':
    # Contoh penggunaan (perlu disesuaikan dengan cara main utama)
    pass