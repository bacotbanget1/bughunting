# Bug Hunting Tool

Alat ini dirancang untuk membantu Developer dan Cyber Security menguji kerentanan umum pada aplikasi web target.

## 🎯 Objek yang Diincar
*   Cross-Site Scripting (XSS)
*   SQL Injection (SQLi)
*   API Key / Token Leakage
*   Celah JavaScript (DOM XSS)

## 🚀 Cara Menjalankan
Gunakan `bug_scanner.py` sebagai *entry point* utama.

**Sintaks:**
`python bug_scanner.py <target_url> <param1> [param2] ...`

**Contoh:**
`python bug_scanner.py http://target.com/page id user_input`

## 🔍 Hasil Deteksi Bug
Jika bug ditemukan, tools akan mencetak detail lengkap:
*   URL yang terinfeksi
*   Parameter yang bermasalah
*   **Severity:** Critical, Medium, Low
*   **Cara Uji:** Instruksi singkat tentang bagaimana bug itu terdeteksi.
*   **Lokasi:** URL parameter yang terpengaruh.

## 🛠️ Struktur Proyek
*   `bug_hunter.py`: Logika dasar XSS dan SQLi.
*   `bug_scanner.py`: Orchestrator utama yang menjalankan semua scan.
*   `tools/api_token_checker.py`: Pengujian kebocoran token/API Key.
*   `tools/js_checker.py`: Pengujian celah JavaScript/DOM XSS.
*   `tools/payloads.py`: Menyimpan daftar payload yang digunakan.

**Catatan:** Pastikan Anda telah menginstal library `requests` (`pip install requests`).