import time
from arc4 import ARC4
from Crypto.Cipher import AES, DES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes


# -----------------------------------------
# DES and AES in CTR mode
# -----------------------------------------
def aes_ctr(key, data, nonce):
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(data)

def des_ctr(key, data, nonce):
    # DES has 8-byte block → use only counter (no prefix)
    ctr = Counter.new(
        64,
        prefix=b"",
        initial_value=int.from_bytes(nonce, "big")
    )
    cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
    return cipher.encrypt(data)


# -----------------------------------------
# Benchmark utility
# -----------------------------------------
def benchmark(fn, *args):
    t0 = time.time()
    output = fn(*args)
    t1 = time.time()
    return t1 - t0


# -----------------------------------------
# MAIN COMPARISON
# -----------------------------------------
def main():
    print("\n=== RC4 (Optimized) vs AES vs DES Performance Test ===\n")

    # Data
    small_data = b"Hello World!" * 1000 # ~12 KB
    large_data = get_random_bytes(2 * 1024 * 1024) # 2 MB

    # Keys
    rc4_key = b"secretkey"
    aes_key = get_random_bytes(16)
    des_key = get_random_bytes(8)
    nonce = get_random_bytes(8)

    # ---------------------- SMALL DATA ----------------------
    print("Testing SMALL data (~12 KB)...")
    rc4_cipher = ARC4(rc4_key)
    t_small_rc4 = benchmark(rc4_cipher.encrypt, small_data)

    t_small_aes = benchmark(aes_ctr, aes_key, small_data, nonce)
    t_small_des = benchmark(des_ctr, des_key, small_data, nonce)

    # ---------------------- LARGE DATA ----------------------
    print("\nTesting LARGE data (2 MB)...")
    rc4_cipher = ARC4(rc4_key)
    t_large_rc4 = benchmark(rc4_cipher.encrypt, large_data)

    t_large_aes = benchmark(aes_ctr, aes_key, large_data, nonce)
    t_large_des = benchmark(des_ctr, des_key, large_data, nonce)

    # ---------------------- RESULTS ----------------------
    print("\n=== PERFORMANCE RESULTS ===")
    print(f"{'Algorithm':<12} {'Size':<10} {'Time (seconds)'}")
    print("-" * 35)
    print(f"RC4 (fast) {'12 KB':<10} {t_small_rc4:.5f}")
    print(f"AES-CTR {'12 KB':<10} {t_small_aes:.5f}")
    print(f"DES-CTR {'12 KB':<10} {t_small_des:.5f}")

    print(f"RC4 (fast) {'2 MB':<10} {t_large_rc4:.5f}")
    print(f"AES-CTR {'2 MB':<10} {t_large_aes:.5f}")
    print(f"DES-CTR {'2 MB':<10} {t_large_des:.5f}")

    print("\nNote:")
    print(" - RC4 here uses the optimized C implementation (very fast).")
    print(" - AES is hardware-accelerated (AES-NI).")
    print(" - DES is slower due to software-only implementation.\n")


if __name__ == "__main__":
    main()
