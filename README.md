# bughunting

Tools ini dirancang untuk membantu Developer dan Cyber Security dalam melakukan bug hunting otomatis pada website target.

## 🎯 Objek yang Diincar
*   Cross-Site Scripting (XSS)
*   SQL Injection (SQLi)
*   API Key / Token Exposure
*   Celah JavaScript
*   Lainnya

## 🚀 Cara Penggunaan
Tools ini dapat dijalankan di berbagai OS (Mac, Linux, Windows, Termux, VPS/RDP) menggunakan Python.

**Contoh Penggunaan (XSS/SQLi):**
```bash
python bug_hunter.py <target_url> <parameter_to_test>
# Contoh: python bug_hunter.py http://target.com/page ?id
```

## 🐞 Pelaporan Bug
Jika bug terdeteksi, tools akan otomatis mencetak detail berikut:
1.  **Bug Ditemukan:** (Contoh: Reflected XSS, SQL Injection)
2.  **URL:** URL lengkap saat bug terpicu.
3.  **Parameter:** Parameter yang diuji.
4.  **Severity:** (Critical, Medium, Low)
5.  **Cara Uji:** (Disebutkan dalam output)
6.  **Lokasi di URL:** (Disebutkan dalam output)

## 🛠️ Struktur Proyek
*   `bug_hunter.py`: Logika utama pengujian (XSS, SQLi).
*   `tools/payloads.py`: Berisi daftar payload untuk berbagai jenis serangan.
*   *(Akan ditambahkan file pengujian API/Token di kemudian hari)*

---
*Disclaimer: Gunakan tools ini hanya pada sistem yang Anda miliki izin eksplisit untuk diuji.*