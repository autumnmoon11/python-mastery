import time
from functools import lru_cache

def fib_naive(n: int) -> int:
    """The 'Standard' but slow way to do Fibonacci."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n: int, cache: dict = None) -> int:
    """Memoized Approach"""
    if cache is None:
        cache = {}
    
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    # Recursive Step + Storing the result in cache
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

@lru_cache(maxsize=None)
def fib_pro(n: int) -> int:
    """The 'Pythonic' Way: Using a decorator to manage the dict"""
    if n <= 1: return n
    return fib_pro(n - 1) + fib_pro(n - 2)

if __name__ == "__main__":
    n = 35
    
    # Test Naive
    start = time.time()
    print(f"Naive Result: {fib_naive(n)} | Time: {time.time() - start:.4f}s")
    
    # Test Memoized (Even with a much larger N)
    large_n = 100
    start = time.time()
    print(f"Memoized Result (N={large_n}): {fib_memo(large_n)} | Time: {time.time() - start:.4f}s")

    # Test Pythonic Memoized with same Large N
    print(f"'Pythonic' Memoized Result (N={large_n}): {fib_pro(large_n)} | Time: {time.time() - start:.4f}s")