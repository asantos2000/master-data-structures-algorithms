import math

def fib_formula(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    val = (golden_ratio**n - (1 - golden_ratio)**n) / math.sqrt(5)
    return int(round(val))

import time

if __name__ == '__main__':
    tic = time.perf_counter()
    res = fib_formula(50)
    toc = time.perf_counter()
    print(f"fib_formula() finishes in {toc - tic:0.8f} seconds")