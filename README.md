# 🔐 RC4 vs AES vs DES – Performance Comparison (Python)

This project implements **RC4**, **AES (CTR)**, and **DES (CTR)** encryption in Python and compares their performance on small and large data sizes.  
It is perfect for academic submissions, benchmarking studies, and cryptography learning.

---

## ✅ Features

- ✔ **Optimized pure-Python RC4 implementation**  
- ✔ **AES & DES using PyCryptodome**  
- ✔ **CTR mode for fair comparison**  
- ✔ **Benchmarks on small (~12 KB) and large (~2 MB) data**  
- ✔ **Performance analysis output**  
- ✔ **PDF report included**  

---

## 📌 Algorithms Overview

### 🔸 RC4 (Stream Cipher)
- Lightweight, simple operations (swap, XOR)
- Fast on small data
- Slows down for large data in Python due to interpreter overhead
- Cryptographically broken — NOT used in modern systems

### 🔸 AES (CTR Mode)
- Modern, secure cipher
- Hardware-accelerated via **AES-NI** on most CPUs
- Extremely fast on large data
- Industry standard

### 🔸 DES (CTR Mode)
- Historical block cipher
- 56-bit key: insecure today  
- Implemented in software → slowest performance

---

## 📦 Installation

Make sure Python 3 is installed.

Install required libraries:

```bash
pip install pycryptodome
