from functools import lru_cache
import timeit

# Top-down approach
# Problema de max recursion depth
@lru_cache
def fibonacci(n):
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

# Top-down approach
def fibonacci_rec_memo(n, f):
    if f[n] == -1:
        f[n] = fibonacci_rec_memo(n - 1, f) + fibonacci_rec_memo(n - 2, f)
    return f[n]

def fibonacci_memo(n):
    f = [-1] * (n + 1)
    f[0] = 0
    f[1] = 1
    return fibonacci_rec_memo(n, f)

# Bottom-up approach
def fibonacci_bottom_up(n):
    if n < 2:
        return n
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def main():
    n = 498 # max recursion depth
    print(fibonacci(n))
    print(fibonacci_memo(n))
    print(fibonacci_bottom_up(n))
    fb = timeit.timeit('fibonacci(n)', setup=f'n={n}', globals=globals(), number=1)
    print(f'memoization com lru_cache: {fb}')
    fb = timeit.timeit('fibonacci_memo(n)', setup=f'n={n}', globals=globals(), number=1)
    print(f'memoization (top-down): {fb}')
    fb = timeit.timeit('fibonacci_bottom_up(n)', setup=f'n={n}', globals=globals(), number=1)
    print(f'memoization (bottom-up): {fb}')

if __name__ == '__main__':
    main()
