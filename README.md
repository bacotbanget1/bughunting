# 🐞 Bug Hunting Tool

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Last Commit](https://img.shields.io/badge/last%20commit-day-green.svg)]()
[![Stars](https://img.shields.io/badge/stars-★★★★★-ffcc00.svg)]()

---

## 🔍 Deskripsi Singkat

**Bug Hunting Tool** adalah paket utilitas open-source untuk deteksi otomatis kerentanan web seperti **XSS**, **SQL Injection**, serta **API Token Leak**. Dirancang untuk developer, security researcher, maupun pemula yang ingin belajar bug bounty dengan pendekatan praktis.

---

## ✨ Fitur Utama

| Fitur | Deskripsi | Kategori |
|-------|-----------|----------|
| **XSS Scanner** | Mendeteksi Reflected XSS pada parameter URL | Web Security |
| **SQLi Scanner** | Menguji SQL Injection (Error-Based) | Web Security |
| **API Token Checker** | Memeriksa kebocoran API Key/Token | Auth Security |
| **JavaScript XSS** | Menguji DOM-based XSS | Web Security |
| **Subdomain Scanner** | Memindai subdomain dari daftar | Recon |
| **Interactive Menu** | Antarmuka CLI yang ramah pengguna | UX |

---

## 📦 Struktur Proyek

```
bacotbanget1/bughunting/
├── main.py                    # Menu interaktif utama
├── bug_hunter.py              # Scanner XSS & SQLi manual
├── bug_scanner.py             # Scanner komprehensif semua tes
├── subdomain_scanner.py       # Scanner subdomain
├── parameter.json             # Daftar parameter untuk scanning
├── subdomain.json             # Daftar domain/subdomain untuk dipindai
└── tools/
    ├── api_token_checker.py   # Deteksi API token/key
    ├── js_checker.py          # Deteksi JavaScript/DOM XSS
    └── payloads.py            # Payload dan regex deteksi
```

---

## 🚀 Instalasi

### Prasyarat
- Python 3.6+
- `requests` library

### Langkah Instalasi

```bash
# Clone repository
git clone https://github.com/bacotbanget1/bughunting.git
cd bughunting

# Install dependencies
pip install requests

# (Opsional) Install semua tools secara bersamaan
pip install -r requirements.txt  # Jika ada
```

---

## 🛠️ Penggunaan

### 1. Menggunakan Menu Interaktif (Disarankan)

```bash
python main.py
```

> Pilih antara:
> - **Scan Manual** → XSS & SQLi
> - **Scan Komprehensif** → Semua tipe keamanan
> - **Scan Subdomain** → Recon domain

---

### 2. Scan Manual (XSS & SQLi)

```bash
python bug_hunter.py <target_url> <parameter>

# Contoh:
python bug_hunter.py http://test.com/search ?q
```

---

### 3. Scan Komprehensif Semua Parameter

```bash
# Dengan parameter manual
python bug_scanner.py http://test.com/search id q page user

# Otomatis membaca dari parameter.json
python bug_scanner.py http://test.com/search
```

---

### 4. Scan Subdomain

```bash
python subdomain_scanner.py
```

> Tool akan membaca domain dari `subdomain.json` dan memverifikasinya secara paralel.

---

## ⚙️ Konfigurasi Payload

Payload utama disimpan di `tools/payloads.py`:

| Tipe | File | Variabel |
|------|------|----------|
| XSS | `payloads.py` | `XSS_PAYLOADS` |
| SQLi | `payloads.py` | `SQLI_PAYLOADS` |
| API Token | `payloads.py` | `TOKEN_CHECK_PAYLOADS` |

Anda dapat menambahkan payload kustom sesuai kebutuhan.

---

## 📊 Contoh Output

```
=====================================================
[!!!] BUG DITEMUKAN: Reflected XSS
    URL: http://test.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E
    Parameter: q
    Severity: Medium
=====================================================
```

---

## ⚠️ Disclaimer

> **Tools ini hanya untuk edukasi dan testing aman di lingkungan yang Anda kontrol.** Penggunaan terhadap sistem tanpa izin adalah pelanggaran hukum. Selalu dapatkan persetujuan sebelum melakukan scanning.

---

## 🤝 Kontribusi

Terbuka untuk kontribusi! Silakan:
1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/amazing-feature`)
3. Commit perubahan (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazign-feature`)
5. Buka Pull Request

---

## 📄 Lisensi

Distribusi di bawah lisensi **MIT**. Lihat file `LICENSE` untuk detail lebih lanjut.

---

## 🙏 Penutup

Semoga tools ini membantu Anda dalam **bug hunting journey**! Jangan lupa untuk:
- ✅ Laporkan bug yang ditemukan
- ✅ Beri bintang ⭐ jika tools ini membantu
- ✅ Ikuti project ini untuk update terbaru

---

**Made with ❤️ by NazamaLint**