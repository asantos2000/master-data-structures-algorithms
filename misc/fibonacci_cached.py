import time
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n==0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) 

tic = time.perf_counter()
res = fibonacci(50)
toc = time.perf_counter()
print(f"fibonacci() finishes in {toc - tic:0.8f} seconds")
# fibonacci() finishes in 0.0001 seconds
