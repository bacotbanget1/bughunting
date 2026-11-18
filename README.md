<div align="center">

# 🐞 Bug Hunting Automation Tool

**Suite pengujian penetrasi web & recon otomatis ringan berbasis Python untuk Security Researcher dan Bug Hunters.**

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-blue.svg?style=for-the-badge)]()
[![Security Rating](https://img.shields.io/badge/Security-Audit%20Ready-red.svg?style=for-the-badge)]()

[Fitur](#-fitur-utama) • [Instalasi](#-instalasi) • [Panduan Penggunaan](#-panduan-penggunaan) • [Struktur Proyek](#-struktur-arsitektur) • [Disclaimer](#-disclaimer-hukum)

</div>

---

## 📖 Tentang Proyek

**Bug Hunting Tool** adalah utilitas keamanan web modular berbasis Python yang dirancang untuk mempercepat tahap *reconnaissance* dan deteksi awal celah keamanan umum pada target web. Tool ini membantu menemukan kelemahan seperti Reflected Cross-Site Scripting (XSS), SQL Injection (Error-Based), kebocoran token/kredensial API, dan pemetaan subdomain aktif secara otomatis.

Cocok digunakan untuk latihan di lab keamanan (DVWA, PortSwigger, CTF) maupun pengujian resmi pada program *Bug Bounty*.

---

## ✨ Fitur Utama

| Modul / Fitur | Deskripsi | Deteksi |
|---|---|---|
| 💉 **Reflected XSS Scanner** | Menginjeksi payload XSS ke parameter URL dan mengevaluasi pantulan (*reflection*) dalam respon HTTP. | Web Vulnerability |
| 🛡️ **SQLi Detector** | Menguji parameter dengan berbagai *vector injection* berbasis sintaks SQL dan mencocokkan error engine basis data (MySQL, PostgreSQL, MSSQL, Oracle). | Web Vulnerability |
| 🔑 **API Token / Key Leak** | Menganalisis parameter atau respon terhadap paparan format token, API keys, dan secret tokens populer. | Information Disclosure |
| 🌐 **DOM / JS Checker** | Memeriksa konteks JavaScript dan sink berbahaya pada frontend target. | Client-side Security |
| 📡 **Subdomain Scanner** | Memvalidasi daftar target subdomain secara cepat dan menentukan ketersediaan host (`HTTP 200 OK`). | Reconnaissance |
| 💻 **CLI Interaktif** | Navigasi menu intuitif dan fleksibel langsung dari terminal. | Usability |

---

## 📂 Struktur Arsitektur

```text
bacotbanget1/bughunting/
├── main.py                    # Menu utama interaktif (entry point)
├── bug_hunter.py              # Scanner terfokus untuk XSS & SQLi manual
├── bug_scanner.py             # Scanner komprehensif berbasis parameter list
├── subdomain_scanner.py       # Multi-target subdomain checker
├── parameter.json             # Daftar kata kunci parameter umum (wordlist)
├── subdomain.json             # Target wordlist domain / subdomain
└── tools/
    ├── api_token_checker.py   # Modul deteksi pola API token / secret
    ├── js_checker.py          # Modul analisis sink JavaScript & DOM
    └── payloads.py            # Koleksi payload exploit & regex database error
```

---

## 🚀 Instalasi

### 1. Prasyarat Sistem
- Python 3.8 ke atas
- Koneksi Internet untuk scanning target eksternal

### 2. Kloning Repository & Pengaturan Environtment

```bash
# Kloning repo
git clone https://github.com/bacotbanget1/bughunting.git
cd bughunting

# (Opsional tapi disarankan) Buat virtual environment
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
# venv\Scripts\activate   # Untuk Windows

# Instalasi dependensi
pip install requests
```

---

## 🛠️ Panduan Penggunaan

### 1. Menu Interaktif (Rekomendasi)
Jalankan antarmuka utama untuk memilih jenis pengujian tanpa perlu menghafal argumen CLI:

```bash
python main.py
```

---

### 2. Manual Scan (Target Spesifik & Parameter Tertentu)
Gunakan `bug_hunter.py` bila Anda ingin menguji endpoint spesifik dengan parameter tunggal:

```bash
python bug_hunter.py <TARGET_URL> <PARAMETER>

# Contoh:
python bug_hunter.py https://example.com/search.php q
```

---

### 3. Comprehensive Scan (Semua Fitur Otomatis)
Gunakan `bug_scanner.py` untuk menguji kerentanan menggunakan daftar parameter:

```bash
# Mode 1: Otomatis memuat parameter dari parameter.json
python bug_scanner.py https://example.com/item

# Mode 2: Menentukan parameter manual secara berurutan
python bug_scanner.py https://example.com/item id search page cat
```

---

### 4. Subdomain Reconnaissance
Lakukan validasi subdomain aktif yang didefinisikan pada `subdomain.json`:

```bash
python subdomain_scanner.py
```

---

## ⚙️ Kustomisasi Wordlist & Payload

Anda dapat menyesuaikan payload dan parameter pengujian langsung pada file konfigurasi:

- **Modifikasi Parameter:** Edit `parameter.json` untuk menambah atau menghapus nama parameter yang sering ditemukan (*e.g.*, `redirect`, `callback`, `file`, dll.).
- **Modifikasi Payload:** Buka `tools/payloads.py`:
  - `XSS_PAYLOADS`: Daftar payload XSS untuk bypass filter umum.
  - `SQLI_PAYLOADS`: Karakter khusus dan kutip penguji sintaks SQL.
  - `SQL_ERRORS`: Signature regex error database.
  - `TOKEN_CHECK_PAYLOADS`: Pola deteksi API key/token.

---

## 📋 Contoh Hasil Deteksi

```text
[+] Memulai pengujian pada target: https://vulnerable-site.test/search
[*] Parameter uji: query
----------------------------------------------------------------------
[!!!] KERENTANAN DITEMUKAN: Reflected XSS
      [>] Payload  : <script>alert(1)</script>
      [>] Parameter: query
      [>] URL Bukti: https://vulnerable-site.test/search?query=%3Cscript%3Ealert(1)%3C/script%3E

[!!!] KERENTANAN DITEMUKAN: Error-Based SQL Injection
      [>] Payload  : ' OR '1'='1
      [>] Pattern  : You have an error in your SQL syntax
----------------------------------------------------------------------
[+] Selesai. Laporan siap dianalisis.
```

---

## ⚠️ Disclaimer Hukum

> **PERINGATAN:** Proyek ini dibuat dan didistribusikan semata-mata untuk **tujuan edukasi, riset keamanan siber, dan penetrasi etis (Ethical Hacking)**. Menguji target web tanpa izin tertulis yang sah dari pemilik sistem adalah tindakan melanggar hukum. Pembuat tidak bertanggung jawab atas kerugian atau tindakan ilegal yang dilakukan oleh pihak mana pun menggunakan perangkat lunak ini.

---

## 🤝 Kontribusi

Kontribusi dari komunitas sangat disambut:
1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/FiturBaru`)
3. Lakukan commit perubahan (`git commit -m 'Menambahkan payload bypass baru'`)
4. Push ke branch Anda (`git push origin feature/FiturBaru`)
5. Buka Pull Request (PR)

---

## 📄 Lisensi

Didistribusikan di bawah lisensi **MIT**. Silakan tinjau file `LICENSE` untuk ketentuan lebih lanjut.