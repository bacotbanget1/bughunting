import sys
import subprocess
import os

def display_menu():
    print("\n=========================================")
    print("🚀 BUG HUNTING TOOL INTERAKTIF")
    print("=========================================")
    print("Pilih Fitur:")
    print("1. Scan Manual (XSS & SQLi) - Menggunakan bug_hunter.py")
    print("2. Scan Komprehensif (Semua Tes) - Menggunakan bug_scanner.py")
    print("3. Scan Subdomain - Menggunakan subdomain_scanner.py")
    print("0. Keluar")
    print("-----------------------------------------")

def get_user_input(prompt, required=True):
    while True:
        user_input = input(prompt).strip()
        if required and not user_input:
            print("Input tidak boleh kosong.")
            continue
        return user_input

def run_feature_1():
    print("\n--- Fitur 1: Scan Manual (XSS & SQLi) ---")
    target_url = get_user_input("Masukkan Target URL (contoh: http://test.com/page): ")
    param = get_user_input("Masukkan Parameter yang akan diuji (contoh: id): ")
    
    if not target_url or not param:
        print("URL dan Parameter wajib diisi untuk Scan Manual.")
        return

    print(f"\n[INFO] Menjalankan: python bug_hunter.py {target_url} {param}")
    try:
        # Menjalankan skrip menggunakan subprocess
        subprocess.run([sys.executable, "bug_hunter.py", target_url, param], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Skrip bug_hunter.py gagal dijalankan: {e}")
    except FileNotFoundError:
        print("[ERROR] Pastikan bug_hunter.py ada di direktori yang sama.")

def run_feature_2():
    print("\n--- Fitur 2: Scan Komprehensif (Semua Tes) ---")
    target_url = get_user_input("Masukkan Target URL (contoh: http://test.com/search): ")
    
    if not target_url:
        print("URL wajib diisi untuk Scan Komprehensif.")
        return
        
    print("\n[INFO] Apakah Anda ingin menentukan parameter secara manual, atau biarkan tool membaca dari parameter.json/default?")
    choice = input("Pilih (M/A) [M=Manual, A=Auto]: ").upper()
    
    parameters = []
    if choice == 'M':
        print("Masukkan parameter satu per satu. Kosongkan input untuk berhenti.")
        while True:
            param = input("Parameter ke-N (kosongkan untuk selesai): ").strip()
            if not param:
                break
            parameters.append(param)
    elif choice == 'A':
        print("[INFO] Tool akan otomatis membaca parameter dari parameter.json atau menggunakan default.")
    else:
        print("Pilihan tidak valid. Menggunakan mode Auto.")

    print(f"\n[INFO] Menjalankan: python bug_scanner.py {target_url} {' '.join(parameters) if parameters else ''}")
    try:
        # Mengirim parameter jika ada, jika tidak, hanya URL
        command = [sys.executable, "bug_scanner.py", target_url] + parameters
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Skrip bug_scanner.py gagal dijalankan: {e}")
    except FileNotFoundError:
        print("[ERROR] Pastikan bug_scanner.py ada di direktori yang sama.")

def run_feature_3():
    print("\n--- Fitur 3: Scan Subdomain ---")
    print("[INFO] Scan ini akan menggunakan daftar domain dari subdomain.json.")
    print("[INFO] Proses ini berjalan secara paralel dan mungkin memakan waktu.")
    
    print("\n[INFO] Menjalankan: python subdomain_scanner.py")
    try:
        subprocess.run([sys.executable, "subdomain_scanner.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Skrip subdomain_scanner.py gagal dijalankan: {e}")
    except FileNotFoundError:
        print("[ERROR] Pastikan subdomain_scanner.py ada di direktori yang sama.")


def main():
    while True:
        display_menu()
        choice = input("Masukkan pilihan (0-3): ").strip()
        
        if choice == '1':
            run_feature_1()
        elif choice == '2':
            run_feature_2()
        elif choice == '3':
            run_feature_3()
        elif choice == '0':
            print("\n👋 Terima kasih telah menggunakan Bug Hunting Tool. Sampai jumpa!")
            break
        else:
            print("\n❌ Pilihan tidak valid. Silakan masukkan angka antara 0 dan 3.")

if __name__ == "__main__":
    main()