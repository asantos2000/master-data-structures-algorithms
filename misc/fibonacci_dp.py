def fib(n):
    new, old = 1, 0
    for _ in range(n):
        new, old = old, new + old
    return old

if __name__ == "__main__":
    print(f'fib(12)={fib(12)}')