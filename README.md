# 🔐 RC4 vs AES vs DES – Performance Comparison (Python)

This project implements and benchmarks three cryptographic algorithms:

- **RC4** (via optimized C-based `arc4` library)
- **AES (CTR Mode)** using PyCryptodome
- **DES (CTR Mode)** using PyCryptodome

It compares performance on small (~12 KB) and large (2 MB) data sizes.  
This project is suitable for academic submissions, demonstrations, and cryptography learning.

---

## ✅ Features

- ✅ Fast RC4 implementation using the **arc4** C library  
- ✅ AES-CTR and DES-CTR using PyCryptodome  
- ✅ Fair benchmarking using Python `time` module  
- ✅ Covers both small and large data cases  
- ✅ Includes PDF report template  
- ✅ Simple and clean codebase  

---

## 📌 Algorithms Overview

### 🔸 RC4 (Stream Cipher)
- Implemented using optimized C extension (`arc4`)
- Very fast for small data
- Slower on very large data compared to AES (because AES uses hardware acceleration)
- Cryptographically insecure today

### 🔸 AES (CTR Mode)
- Industry standard encryption algorithm
- Uses **AES-NI** hardware acceleration on modern CPUs
- Fastest for large data
- Strong security and widely used

### 🔸 DES (CTR Mode)
- Historical block cipher (56-bit key)
- Slower due to no hardware acceleration
- Considered insecure today

---

## 📦 Installation

Install dependencies:
pip install pycryptodome arc4


Running the Benchmark:
python CCS.py


=== RESULTS ===
Algorithm Size Time (s)
RC4 | 12 KB | 0.0009
AES-CTR | 12 KB | 0.02045
DES-CTR | 12 KB | 0.00099

RC4 | 2 MB | 0.01211
AES-CTR | 2 MB | 0.00527
DES-CTR | 2 MB | 0.05569
