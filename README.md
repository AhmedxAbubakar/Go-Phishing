# 🛡️ Phishing Email Analyzer

This is a Python-based phishing detection tool that scans email bodies for common phishing indicators using regular expressions and a basic scoring system.

## 🚀 Features

- Detects suspicious elements such as:
  - URLs and shortened links (e.g., bit.ly, tinyurl)
  - Urgent language and social engineering tactics
  - Trigger phrases (e.g., "verify account", "click here")
  - Attachments or file references
  - Possible spoofing patterns

- Outputs a **risk level**: Low, Medium, or High
- Provides details on what was detected

---

## 🧪 How to Use

1. **Install Python** (if not already installed):  
   [Download Python](https://www.python.org/downloads/)

2. **Clone or copy this script** to your local machine.

3. **Run the script**:
   ```bash
   python phishing_analyzer.py
