# 🛡️ Bug Hunting & Vulnerability Scanner

Alat ini adalah *scanner* otomatis yang dirancang untuk membantu **Developer** dan **Cyber Security Professional** mengidentifikasi kerentanan umum pada aplikasi web target secara efisien.

## 🎯 Objek Pengujian Utama
*   **Cross-Site Scripting (XSS):** Reflected dan potensi DOM XSS.
*   **SQL Injection (SQLi):** Deteksi berbasis *error* database.
*   **API Key / Token Leakage:** Pengujian kebocoran kredensial sensitif.
*   **Celah JavaScript:** Pengujian manipulasi sisi klien.

## 🚀 Cara Menjalankan (Entry Point)
Gunakan `bug_scanner.py` sebagai *entry point* utama.

**Prasyarat:** Pastikan Python terinstal dan instal library `requests`:
`pip install requests`

**Sintaks:**
`python bug_scanner.py <target_url> <param1> [param2] ...`

**Contoh Penggunaan:**
`python bug_scanner.py http://target.com/page id user_input`

## 🔍 Laporan Deteksi Bug
Jika kerentanan terdeteksi, tools akan mencetak laporan terstruktur:
*   **URL Terinfeksi:** URL lengkap saat bug terpicu.
*   **Parameter Bermasalah:** Parameter yang menjadi vektor serangan.
*   **Severity:** **Critical**, **Medium**, atau **Low**.
*   **Cara Uji:** Instruksi singkat mengenai mekanisme deteksi.
*   **Lokasi:** URL parameter yang terpengaruh.

## 🛠️ Struktur Proyek
*   `bug_scanner.py`: **Orchestrator** utama yang mengkoordinasikan semua pengujian.
*   `bug_hunter.py`: Implementasi logika dasar untuk XSS dan SQLi.
*   `tools/api_token_checker.py`: Logika pengujian kebocoran token/API Key.
*   `tools/js_checker.py`: Logika pengujian celah JavaScript/DOM XSS.
*   `tools/payloads.py`: Menyimpan semua daftar payload yang digunakan.

---
*Disclaimer: Gunakan alat ini hanya pada sistem yang Anda miliki izin eksplisit untuk diuji (misalnya, lingkungan staging atau lab pribadi).*