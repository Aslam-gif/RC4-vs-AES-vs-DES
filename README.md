RC4, AES, and DES Performance Comparison Report:

Aslam Siddhiq A,
3rd Year CSE student

1. Introduction
This updated report includes encryption and decryption timings for RC4 (arc4 optimized),
AES-CTR, and DES-CTR. Large data blocks of 5 MB and 25 MB were used, as requested.


2. Algorithms Overview
- RC4 (arc4): Stream cipher implemented as a C extension for high speed.
- AES-CTR: Modern secure cipher using hardware acceleration (AES-NI).
- DES-CTR: Old, insecure cipher; slow and purely software-based.


3. Methodology
Two large random test blocks were used:
- 5 MB block
- 25 MB block
Both encryption and decryption phases were benchmarked using timing functions.


4. Benchmark Table:
--- Testing Block Size: 5 MB ---
RC4 | Encrypt: 0.0086s | Decrypt: 0.0089s
AES-CTR | Encrypt: 0.0118s | Decrypt: 0.0061s
DES-CTR | Encrypt: 0.0976s | Decrypt: 0.0729s

--- Testing Block Size: 25 MB ---
RC4 | Encrypt: 0.0421s | Decrypt: 0.0459s
AES-CTR | Encrypt: 0.0343s | Decrypt: 0.0290s
DES-CTR | Encrypt: 0.3000s | Decrypt: 0.2876s


5. Analysis
- RC4 performs very fast on medium data but slows for very large blocks.
- AES-CTR remains the fastest due to CPU-level AES-NI acceleration.
- DES-CTR is consistently the slowest because of outdated design and software-only execution.


6. Conclusion
AES is the best-performing and most secure option. RC4 is moderately fast but insecure.
DES is outdated and slow. Large-block tests clearly show the advantage of hardware-backed
cryptographic algorithms like AES.


7. Notes
This benchmark highlights how algorithm complexity and hardware support influence real-world
performance.

Output:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/983d51a8-f97c-41e0-a7f6-8585cfdae61a" />



Install dependencies:
pip install pycryptodome arc4


Running the Benchmark:
python CCS.py


Result:
RC4 performs better on small datasets but lags behind AES on large datasets due to Python
interpretation overhead.
AES remains the fastest and most secure due to hardware acceleration.
DES demonstrates the slowest performance and is insecure for modern cryptographic use.





