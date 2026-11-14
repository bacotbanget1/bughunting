# 🛡️ Bug Hunting & Vulnerability Scanner

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge&logo=github&logoColor=white" alt="Contributions Welcome">
  <img src="https://img.shields.io/badge/Made%20for-Bug%20Bounty-red?style=for-the-badge&logo=hackerone&logoColor=white" alt="Bug Bounty">
</p>

<p align="center">
  <b>Automated vulnerability scanner designed for Developers & Cyber Security Professionals to identify common web application flaws efficiently.</b>
</p>

---

## 🎯 **Key Features (Test Coverage)**

| Vulnerability Type | Detection Method | Severity Mapping |
| :--- | :--- | :--- |
| **Cross-Site Scripting (XSS)** | Reflected & DOM-based Payload Injection | `Critical` / `Medium` |
| **SQL Injection (SQLi)** | Error-based Database Fingerprinting | `Critical` / `High` |
| **API Key / Token Leakage** | Regex Pattern Matching & Validation | `High` / `Medium` |
| **JavaScript / DOM Sinks** | Static Analysis & Sink Tracing | `Medium` / `Low` |

---

## 🚀 **Quick Start**

### **Prerequisites**
*   Python **3.8+**
*   `requests` library

### **Installation**
```bash
# 1. Clone the repository
git clone https://github.com/bacotbanget1/bughunting.git
cd bughunting

# 2. Install dependencies
pip install -r requirements.txt
# Or manually: pip install requests
```

### **Usage (Entry Point: `bug_scanner.py`)**
```bash
# Syntax
python bug_scanner.py <TARGET_URL> <PARAM_1> [PARAM_2] ...

# Examples
python bug_scanner.py "https://example.com/search" "q"
python bug_scanner.py "https://api.target.com/v1/users" "id" "email" "token"
```

---

## 📊 **Sample Output Report**

When a vulnerability is detected, the tool outputs a structured JSON/Console report:

```text
[+] VULNERABILITY DETECTED
--------------------------------------------------
[🔴 SEVERITY]       : CRITICAL
[🐛 TYPE]           : SQL Injection (Error Based)
[🎯 PARAMETER]      : id
[🔗 INFECTED URL]   : https://target.com/page?id=1%27
[📝 PAYLOAD USED]   : ' UNION SELECT NULL,@@version-- 
[💡 EVIDENCE]       : MySQL Syntax Error detected in response
[🛠️ REMEDIATION]    : Use Parameterized Queries / Prepared Statements
--------------------------------------------------
```

---

## 🏗️ **Project Architecture**

```text
bughunting/
├── 📄 bug_scanner.py          # 🎮 Main Orchestrator / CLI Entry Point
├── 📄 bug_hunter.py           # 🧠 Core Logic: XSS & SQLi Engines
├── 📄 requirements.txt        # 📦 Dependencies
├── 📁 tools/
│   ├── 📄 api_token_checker.py  # 🔑 Secrets & Token Detection
│   ├── 📄 js_checker.py         # 📜 JS/DOM XSS Sink Analysis
│   └── 📄 payloads.py           # 💣 Centralized Payload Repository
└── 📄 README.md               # 📖 This File
```

### **Module Responsibilities**
*   **`bug_scanner.py`**: Handles argument parsing, target normalization, multi-threading coordination, and report aggregation.
*   **`bug_hunter.py`**: Implements the fuzzing logic for Reflected XSS and Error-Based SQLi (boolean/error based).
*   **`tools/api_token_checker.py`**: Scans responses for high-entropy strings, JWTs, AWS Keys, GitHub Tokens, Generic API Keys.
*   **`tools/js_checker.py`**: Identifies dangerous sinks (`innerHTML`, `eval`, `location.hash`) in JS files linked from target.
*   **`tools/payloads.py`**: Maintains categorized, encoded, and WAF-bypass payload lists.

---

## ⚙️ **Configuration & Customization**

Edit **`tools/payloads.py`** to:
*   Add custom WAF bypass payloads.
*   Adjust payload encoding levels (URL, Double URL, Unicode, Base64).
*   Define technology-specific SQLi payloads (MySQL, Postgres, MSSQL, Oracle).

---

## 🤝 **Contributing**

Contributions are what make the open-source community amazing. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## ⚖️ **License**

Distributed under the **MIT License**. See `LICENSE` file for more information.

---

## ⚠️ **Legal Disclaimer**

> **⚠️ FOR AUTHORIZED TESTING ONLY**
>
> This tool is designed for **educational purposes** and **authorized security assessments** (Bug Bounty Programs, CTFs, Private Labs, Penetration Testing engagements with written permission).
>
> **Unauthorized scanning or testing of systems you do not own or have explicit permission to test is ILLEGAL and UNETHICAL.**
>
> The authors assume **no liability** and are **not responsible** for any misuse or damage caused by this program.

---

## 👨‍💻 **Author & Contact**

<p align="left">
  <a href="https://github.com/bacotbanget1" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-bacotbanget1-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile">
  </a>
  <a href="https://github.com/bacotbanget1/bughunting/issues" target="_blank">
    <img src="https://img.shields.io/badge/Report_Issue-Bug_Report-red?style=for-the-badge&logo=github&logoColor=white" alt="Issue Tracker">
  </a>
</p>

---

<p align="center">
  <i>If you find this project useful, please consider giving it a ⭐ Star!</i>
</p>