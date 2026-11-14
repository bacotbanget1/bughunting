import requests
import concurrent.futures
import threading
from urllib.parse import urljoin

# Global set untuk melacak subdomain unik
found_subdomains = set()
lock = threading.Lock()

def check_subdomain(domain):
    """
    Fungsi placeholder untuk mengecek subdomain. 
    CATATAN: Dalam implementasi nyata, ini memerlukan brute-forcing (misal: menggunakan wordlist) 
    atau layanan OSINT (misal: VirusTotal, Amass). 
    Karena tidak ada tool eksternal, ini hanya simulasi pengecekan dasar.
    """
    print(f"[*] Mencoba memverifikasi domain: {domain}")
    
    # Simulasi: Cek apakah domain utama bisa diakses
    base_url = f"http://{domain}"
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code < 400:
            with lock:
                found_subdomains.add(domain)
            print(f"[+] Domain {domain} dapat diakses (Status: {response.status_code}).")
    except requests.exceptions.RequestException:
        # Gagal koneksi, anggap bukan subdomain aktif untuk saat ini
        pass

def scan_subdomains(domain_list):
    """Menjalankan scanning secara paralel."""
    print("\n=====================================================")
    print("🚀 MEMULAI SUBDOMAIN SCANNER")
    print("=====================================================")
    
    # Menggunakan ThreadPoolExecutor untuk paralelisme
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_subdomain, domain_list)
        
    print("\n=====================================================")
    print("✅ SUBDOMAIN SCANNING SELESAI")
    print("=====================================================")
    
    if found_subdomains:
        print("\n--- DAFTAR SUBDOMAIN DITEMUKAN ---")
        for subdomain in sorted(list(found_subdomains)):
            print(f"-> {subdomain}")
        print("----------------------------------")
    else:
        print("❌ Tidak ada subdomain aktif yang terdeteksi dari daftar.")

if __name__ == '__main__':
    import sys
    try:
        with open("subdomain.json", 'r') as f:
            domains = json.load(f)
    except FileNotFoundError:
        print("Error: subdomain.json tidak ditemukan.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Format subdomain.json tidak valid.")
        sys.exit(1)
        
    scan_subdomains(domains)