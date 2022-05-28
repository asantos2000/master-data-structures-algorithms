import random

i = 1
n = 4
while True:
    # Certificate or guesses
    x = [random.randint(0, 1) for _ in range(n)]
    # Verification
    if (x[0] or x[1] or x[2]) and (not x[0] or x[1] or x[2]) and (x[0] or not x[1] or x[2]) and (not x[0] or not x[1] or x[3]):
        print(x)
        break
    i += 1
print(i)

i = 1
n = 3
while True:
    # Certificate or guesses
    x = [random.randint(0, 1) for _ in range(n)]
    # Verification
    if (not x[0] or not x[1] or not x[2]) and (x[0] or x[1] or x[2]):
        print(x)
        break
    i += 1
print(i)