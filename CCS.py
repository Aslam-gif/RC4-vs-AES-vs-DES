import time
from arc4 import ARC4
from Crypto.Cipher import AES, DES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes

# -----------------------------
# AES CTR Mode
# -----------------------------
def aes_ctr_encrypt(key, data, nonce):
ctr = Counter.new(64, prefix=nonce)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
return cipher.encrypt(data)

def aes_ctr_decrypt(key, data, nonce):
ctr = Counter.new(64, prefix=nonce)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
return cipher.decrypt(data)

# -----------------------------
# DES CTR Mode
# -----------------------------
# DES CTR FIX
def des_ctr_encrypt(key, data, nonce):
ctr = Counter.new(
64,
prefix=b"",

initial_value=int.from_bytes(nonce, "big")
)
cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
return cipher.encrypt(data)
def des_ctr_decrypt(key, data, nonce):
ctr = Counter.new(
64,
prefix=b"",
initial_value=int.from_bytes(nonce, "big")
)
cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
return cipher.decrypt(data)

# -----------------------------
# Benchmark Function
# -----------------------------
def benchmark(fn, *args):
t0 = time.time()
output = fn(*args)
t1 = time.time()
return t1 - t0, output

# -----------------------------
# MAIN
# -----------------------------
def main():
print("\n=== RC4 vs AES vs DES (Encryption + Decryption) ===\n")

# Large blocks (as your professor requested)
# Change these simply if needed
BLOCK1 = 5 * 1024 * 1024 # 5 MB
BLOCK2 = 25 * 1024 * 1024 # 25 MB (very large block)
data1 = get_random_bytes(BLOCK1)
data2 = get_random_bytes(BLOCK2)

rc4_key = b"secretkey"
aes_key = get_random_bytes(16)
des_key = get_random_bytes(8)
nonce = get_random_bytes(8)

tests = [(data1, "5 MB"), (data2, "25 MB")]

for data, label in tests:
print(f"\n--- Testing Block Size: {label} ---")

# RC4
rc4 = ARC4(rc4_key)
enc_time, enc_out = benchmark(rc4.encrypt, data)

rc4 = ARC4(rc4_key)
dec_time, _ = benchmark(rc4.decrypt, enc_out)

print(f"RC4 | Encrypt: {enc_time:.4f}s | Decrypt: {dec_time:.4f}s")

# AES
enc_time, enc_out = benchmark(aes_ctr_encrypt, aes_key, data, nonce)
dec_time, _ = benchmark(aes_ctr_decrypt, aes_key, enc_out, nonce)
print(f"AES-CTR | Encrypt: {enc_time:.4f}s | Decrypt: {dec_time:.4f}s")

# DES
enc_time, enc_out = benchmark(des_ctr_encrypt, des_key, data, nonce)
dec_time, _ = benchmark(des_ctr_decrypt, des_key, enc_out, nonce)
print(f"DES-CTR | Encrypt: {enc_time:.4f}s | Decrypt: {dec_time:.4f}s")

print("\nNote:")
print(" - RC4 uses the arc4 optimized C implementation.")
print(" - AES uses AES-NI hardware acceleration.")
print(" - DES is software-only and slow.")

if __name__ == "__main__":
main()

