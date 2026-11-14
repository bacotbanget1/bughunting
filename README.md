# Bug Hunting Tool

Repositori ini menyediakan serangkaian skrip untuk pengujian keamanan dasar (XSS, SQLi, Token Leak) pada target web.

### 🚀 Cara Instalasi
1. Pastikan Python terinstal di sistem Anda.
2. Instal dependensi yang dibutuhkan:
   `pip install requests`
3. Jalankan melalui antarmuka interaktif:
   `python main.py`

### 💡 Cara Penggunaan Utama
Gunakan `main.py` untuk antarmuka interaktif yang mudah. Pilih fitur dari menu, masukkan URL target, dan masukkan parameter yang ingin diuji (jika diperlukan).

### ✨ Fitur yang Tersedia di Menu:
1. **Bug Hunter Manual:** Uji XSS & SQLi pada URL dan parameter spesifik.
2. **Bug Scanner Komprehensif:** Jalankan semua pengujian (XSS, SQLi, Token, JS XSS) pada parameter yang ditentukan.
3. **Subdomain Scanner:** Memindai domain dari `subdomain.json`.

### ⚙️ Penggunaan Skrip Asli (Jika diperlukan):
* **`bug_hunter.py`**: Scan manual. Contoh: `python bug_hunter.py <URL> <PARAM>`
* **`bug_scanner.py`**: Scan otomatis/parsial. Contoh: `python bug_scanner.py <URL> [PARAM1] [PARAM2]...`
* **`subdomain_scanner.py`**: Scan subdomain. Contoh: `python subdomain_scanner.py`