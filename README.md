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
├── bug_scanner.py            # Entry point utama — menjalankan semua pengujian sekaligus
├── bug_hunter.py              # Engine inti: pengujian XSS & SQL Injection
├── tools/
│   ├── api_token_checker.py   # Deteksi kebocoran API Key / Token
│   ├── js_checker.py          # Deteksi JavaScript / DOM XSS
│   └── payloads.py            # Daftar payload terpusat (XSS, SQLi, Token)
└── README.md                  # Dokumen ini
```

### Tanggung Jawab Tiap Modul
- **`bug_scanner.py`** — menerima URL target dan daftar parameter dari command line, lalu menjalankan seluruh modul pengujian (XSS, SQLi, token leak, JS XSS) untuk setiap parameter secara berurutan.
- **`bug_hunter.py`** — berisi fungsi `check_xss()` dan `check_sqli()` yang dipakai baik secara mandiri maupun dipanggil oleh `bug_scanner.py`.
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
git clone https://github.com/USERNAME/bughunting.git
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

### 1. Scan Lengkap (Disarankan) — `bug_scanner.py`

Menjalankan **semua** modul pengujian (XSS, SQLi, API Token Leak, JS XSS) sekaligus untuk satu atau beberapa parameter.

```bash
python bug_scanner.py <TARGET_URL> <PARAM_1> [PARAM_2] [PARAM_3] ...
```

**Contoh:**
```bash
python bug_scanner.py "https://example.com/search" "q"

python bug_scanner.py "https://api.target.com/v1/users" "id" "email" "token"
```

### 2. Scan Manual (XSS & SQLi saja) — `bug_hunter.py`

Berguna jika hanya ingin menguji satu parameter untuk XSS & SQL Injection tanpa modul lainnya.

```bash
python bug_hunter.py <TARGET_URL> <PARAMETER>
```

**Contoh:**
```bash
python bug_hunter.py "http://test.com/page" "id"
```

### 3. Scan Khusus JS/DOM XSS — `tools/js_checker.py`

Dapat dijalankan secara independen untuk fokus menguji celah DOM-based XSS.

```bash
python tools/js_checker.py <TARGET_URL> <PARAMETER>
```

**Contoh:**
```bash
python tools/js_checker.py "http://test.com/page" "redirect"
```

---

## 📊 Contoh Output

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
