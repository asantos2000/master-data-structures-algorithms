def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

import time

if __name__ == '__main__':
    tic = time.perf_counter()
    res = fib_iterative(50)
    toc = time.perf_counter()
    print(f" fibonacci() finishes in {toc - tic:0.8f} seconds")