def fibonacci(n):
    if n == 0:
        return 0
    if 0 > n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

import time

if __name__ == '__main__':
    # print(f'0: {fibonacci(0)}')
    # print(f'1: {fibonacci(1)}')
    # print(f'2: {fibonacci(2)}')
    # print(f'3: {fibonacci(3)}')
    # print(f'4: {fibonacci(4)}')
    # print(f'5: {fibonacci(5)}')
    # print(f'6: {fibonacci(6)}')
    # print(f'7: {fibonacci(7)}')
    # print(f'8: {fibonacci(8)}')
    # print(f'9: {fibonacci(9)}')
    # print(f'10: {fibonacci(10)}')

    tic = time.perf_counter()
    res = fibonacci(50)
    toc = time.perf_counter()
    print(f" fibonacci() finishes in {toc - tic:0.8f} seconds")