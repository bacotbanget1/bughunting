# Bug Hunting Tool Suite

Aplikasi ini adalah suite pengujian keamanan otomatis (XSS, SQLi, Token Leak, JS Celah) yang dirancang untuk developer dan profesional keamanan siber.

## 🚀 Cara Menjalankan
Semua pengujian dapat diorkestrasi melalui `bug_scanner.py` (yang akan saya buatkan setelah ini untuk integrasi penuh).

**Contoh Penggunaan (Setelah integrasi):**
`python bug_scanner.py <TARGET_URL> <PARAMETER_1> <PARAMETER_2> ...`

## 🛠️ Modul yang Tersedia
*   **`bug_hunter.py`**: Menguji Reflected XSS dan SQL Injection dasar.
*   **`tools/api_token_checker.py`**: Mencari kebocoran API Key/Token.
*   **`tools/js_checker.py`**: Menguji celah JavaScript/DOM XSS.
*   **`tools/payloads.py`**: Menyimpan semua payload yang digunakan.

## 🚨 Pelaporan Bug
Jika bug terdeteksi, output akan mencakup:
*   URL yang terinfeksi
*   Parameter yang bermasalah
*   **Severity** (Critical, Medium, Low)
*   **Cara Uji**: Instruksi singkat tentang bagaimana bug terdeteksi.
*   **Lokasi**: URL parameter yang rentan.

**Catatan:** Tool ini adalah alat bantu *discovery* dan **bukan pengganti** pengujian manual yang mendalam. Selalu pastikan Anda memiliki izin eksplisit dari pemilik target sebelum melakukan pengujian.