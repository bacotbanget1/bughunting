# 🐛 Bug Hunting & Vulnerability Scanner

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white" alt="Status">
  <img src="https://img.shields.io/badge/Made%20for-Bug%20Bounty-red?style=for-the-badge&logo=hackerone&logoColor=white" alt="Bug Bounty">
</p>

<p align="center">
  <b>Scanner kerentanan otomatis untuk membantu Developer & Security Researcher mendeteksi celah umum pada aplikasi web secara cepat.</b>
</p>

---

## 📋 Daftar Isi

- [Fitur Utama](#-fitur-utama)
- [Struktur Proyek](#-struktur-proyek)
- [Instalasi](#-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Contoh Output](#-contoh-output)
- [Konfigurasi Payload](#-konfigurasi-payload)
- [Disclaimer](#-disclaimer)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)

---

## ✨ Fitur Utama

| Jenis Kerentanan | Modul | Metode Deteksi | Severity |
| :--- | :--- | :--- | :--- |
| **Cross-Site Scripting (XSS)** | `bug_hunter.py` | Reflected payload injection, cek refleksi di body response | Medium |
| **SQL Injection (SQLi)** | `bug_hunter.py` | Error-based fingerprinting (pesan error MySQL/Postgres) | Critical |
| **API Key / Token Leakage** | `tools/api_token_checker.py` | Injeksi payload token & pencarian kata kunci sensitif (`admin`, `secret`) | Critical |
| **JavaScript / DOM XSS** | `tools/js_checker.py` | Payload berbasis eksekusi JS sisi klien, cek refleksi di source | Medium |

Semua payload yang digunakan disimpan terpusat di `tools/payloads.py` sehingga mudah ditambah atau disesuaikan.

---

## 🏗️ Struktur Proyek

```text
bughunting/
├── main.py                    # 🎮 Entry point utama — menu interaktif
├── subdomain.json              # 📝 Daftar subdomain target untuk Subdomain Scanner
├── parameter.json              # 📝 Daftar parameter target untuk Full Web Scanning
├── bug_scanner.py              # Orchestrator pengujian (dipanggil dari menu)
├── bug_hunter.py                # Engine inti: pengujian XSS & SQL Injection
├── tools/
│   ├── api_token_checker.py     # Deteksi kebocoran API Key / Token
│   ├── js_checker.py             # Deteksi JavaScript / DOM XSS
│   └── payloads.py               # Daftar payload terpusat (XSS, SQLi, Token)
└── README.md                   # Dokumen ini
```

### Tanggung Jawab Tiap Modul
- **`main.py`** — titik masuk utama proyek. Menampilkan menu interaktif agar pengguna tinggal memilih mode scanning yang diinginkan, tanpa perlu menghafal argumen command line.
- **`subdomain.json`** — tempat mendaftarkan subdomain yang ingin di-scan melalui menu **Subdomain Scanner**.
- **`parameter.json`** — tempat mendaftarkan target URL & parameter yang ingin di-scan melalui menu **Full Web Scanning**.
- **`bug_scanner.py`** — orchestrator yang menjalankan seluruh modul pengujian (XSS, SQLi, token leak, JS XSS) untuk tiap parameter, dipanggil dari menu di `main.py`.
- **`bug_hunter.py`** — berisi fungsi `check_xss()` dan `check_sqli()` yang dipakai oleh `bug_scanner.py`.
- **`tools/api_token_checker.py`** — mencoba beberapa payload token/API key pada parameter target dan menandai respons yang berpotensi membocorkan data sensitif.
- **`tools/js_checker.py`** — mengirim payload yang menargetkan eksekusi JavaScript sisi klien dan memeriksa apakah payload tersebut terefleksi di response.
- **`tools/payloads.py`** — pusat penyimpanan seluruh payload dan regex deteksi yang dipakai oleh modul-modul di atas.

---

## ⚙️ Instalasi

### Prasyarat
- Python **3.8** atau lebih baru
- Library `requests`

### Langkah-langkah

```bash
# 1. Clone repository
git clone https://github.com/bacotbanget1/bughunting.git
cd bughunting

# 2. (Opsional tapi disarankan) Buat virtual environment
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependency
pip install requests
```

> 💡 Jika ingin membuat `requirements.txt` sendiri, cukup isi dengan satu baris: `requests`.

---

## 🚀 Cara Penggunaan

Cukup jalankan **satu file**, lalu pilih mode scanning yang diinginkan lewat menu interaktif — tidak perlu menghafal argumen command line satu per satu.

```bash
python main.py
```

Setelah dijalankan, akan muncul menu untuk memilih jenis scanning, misalnya **Subdomain Scanner** atau **Full Web Scanning**. Sebelum menjalankan menu tersebut, daftarkan dulu target yang ingin di-scan di file konfigurasi terkait (lihat di bawah).

### 1. 🌐 Subdomain Scanner — via `subdomain.json`

Gunakan menu ini untuk memindai sekumpulan subdomain sekaligus.

1. Buka file `subdomain.json`.
2. Masukkan/tambahkan subdomain target yang ingin diuji, contoh:
   ```json
   {
     "subdomains": [
       "api.example.com",
       "dev.example.com",
       "staging.example.com"
     ]
   }
   ```
3. Jalankan `python main.py`, lalu pilih menu **Subdomain Scanner**.

### 2. 🕸️ Full Web Scanning — via `parameter.json`

Gunakan menu ini untuk memindai URL beserta parameter yang ingin diuji (XSS, SQLi, Token Leak, JS/DOM XSS).

1. Buka file `parameter.json`.
2. Masukkan/tambahkan target URL dan parameter yang ingin diuji, contoh:
   ```json
   {
     "targets": [
       {
         "url": "https://example.com/search",
         "parameters": ["q"]
       },
       {
         "url": "https://api.target.com/v1/users",
         "parameters": ["id", "email", "token"]
       }
     ]
   }
   ```
3. Jalankan `python main.py`, lalu pilih menu **Full Web Scanning**.

> 💡 Format persis field di `subdomain.json` dan `parameter.json` mengikuti apa yang dibaca oleh `main.py` — sesuaikan contoh di atas bila struktur key pada file JSON kamu sedikit berbeda.

---

## 📊 Contoh Output

**Tampilan menu saat `main.py` dijalankan:**
```text
=====================================================
          🐛 BUG HUNTING & VULNERABILITY SCANNER
=====================================================
[1] Subdomain Scanner      (baca dari subdomain.json)
[2] Full Web Scanning      (baca dari parameter.json)
[0] Keluar

Pilih menu >> 2
```

**Contoh hasil scan setelah memilih menu:**
```text
=====================================================
[*] MENGUJI PARAMETER: id
=====================================================
[*] Menguji XSS pada parameter: id
[+] XSS tidak terdeteksi pada percobaan ini.
[*] Menguji SQLi pada parameter: id
=====================================================
[!!!] BUG DITEMUKAN: SQL Injection (Error Based)
    URL: https://target.com/page?id=%27+OR+1%3D1+--+
    Parameter: id
    Severity: Critical
=====================================================
[*] Menguji API Key/Token pada parameter: id
[+] Pengujian API Key/Token tidak terdeteksi pada percobaan ini.
[*] Menguji Celah JavaScript/DOM XSS pada parameter: id
[+] Celah JavaScript/DOM XSS tidak terdeteksi pada percobaan ini.
```

---

## 🔧 Konfigurasi Payload

Semua payload dapat disesuaikan langsung di `tools/payloads.py`:

```python
XSS_PAYLOADS = [...]       # Daftar payload XSS
SQLI_PAYLOADS = [...]      # Daftar payload SQL Injection
TOKEN_CHECK_PAYLOADS = [...]  # Daftar payload pengujian token/API key
```

Tambahkan payload baru sesuai kebutuhan, misalnya payload khusus untuk bypass WAF atau payload yang ditargetkan ke teknologi backend tertentu (MySQL, PostgreSQL, MSSQL, dll).

---

## ⚠️ Disclaimer

> **HANYA UNTUK PENGUJIAN YANG SAH (AUTHORIZED TESTING)**
>
> Tool ini dibuat untuk **tujuan edukasi** dan **pengujian keamanan yang sah** (program Bug Bounty, CTF, lab privat, atau penetration testing dengan izin tertulis dari pemilik sistem).
>
> **Melakukan scanning atau pengujian terhadap sistem yang bukan milik Anda atau tanpa izin eksplisit adalah ILEGAL.**
>
> Penulis tidak bertanggung jawab atas segala bentuk penyalahgunaan atau kerusakan yang ditimbulkan dari penggunaan tool ini.

---

## 🤝 Kontribusi

Kontribusi sangat diterima untuk mengembangkan tool ini lebih lanjut:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/FiturBaru`)
3. Commit perubahan (`git commit -m 'Menambahkan FiturBaru'`)
4. Push ke branch (`git push origin feature/FiturBaru`)
5. Buka Pull Request

---

## ⚖️ Lisensi

Didistribusikan di bawah **Lisensi MIT**. Lihat file `LICENSE` untuk detail lengkap.

---

<p align="center">
  <i>Jika proyek ini bermanfaat, jangan lupa beri ⭐ Star!</i>
</p>
