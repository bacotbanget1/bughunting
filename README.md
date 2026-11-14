# Bug Hunting Tool

Repositori ini berisi serangkaian skrip untuk melakukan pengujian keamanan dasar (XSS, SQLi, Token Leak) pada target web.

### Cara Penggunaan

### 1. Scan Lengkap (Disarankan) — `bug_scanner.py`

Menjalankan **semua** modul pengujian (XSS, SQLi, API Token Leak, JS XSS) sekaligus.

**Jika parameter diberikan di CLI:**
```bash
python bug_scanner.py <TARGET_URL> <PARAM_1> [PARAM_2] ...
```
**Contoh:**
```bash
python bug_scanner.py "https://example.com/search" "q"
```

**Jika TIDAK ada parameter di CLI (Full Scan Otomatis):**
Tool akan secara otomatis membaca daftar parameter dari **`parameter.json`**. Jika file tersebut tidak ada, tool akan menggunakan daftar parameter umum (`id`, `q`, `page`, `user`).
```bash
python bug_scanner.py <TARGET_URL>
```
**Contoh:**
```bash
python bug_scanner.py "https://example.com/profile"
```

### 2. Scan Manual (XSS & SQLi saja) — `bug_hunter.py`
...