def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

for index, x in enumerate(fib()):
    print(f"{x}", end='')
    if index == 10:
        break
    else:
        print(', ', end='')
print()