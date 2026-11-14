...
### Cara Penggunaan

### 1. Scan Lengkap (Disarankan) — `bug_scanner.py`

Menjalankan **semua** modul pengujian (XSS, SQLi, API Token Leak, JS XSS) sekaligus.

**Jika parameter diberikan:**
```bash
python bug_scanner.py <TARGET_URL> <PARAM_1> [PARAM_2] [PARAM_3] ...
```
**Contoh:**
```bash
python bug_scanner.py "https://example.com/search" "q"
```

**Jika TIDAK ada parameter (Full Scan Otomatis):**
Tool akan secara otomatis mencoba parameter umum (`id`, `q`, `page`, `user`) pada URL target.
```bash
python bug_scanner.py <TARGET_URL>
```
**Contoh:**
```bash
python bug_scanner.py "https://example.com/profile"
```

### 2. Scan Manual (XSS & SQLi saja) — `bug_hunter.py`
...