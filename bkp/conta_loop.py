import math

def o_n(n):
    c = 0
    for i in range(n):
        c = c + 1
    return c

def o_n2(n):
    c = 0
    for i in range(n):
        for j in range(n):
            c = c + 1
    return c

def o_nlogn(n):
    c = 0
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            c = c + 1
            j = j + i
        i = i + 1
    return c

def o_sqrt_n(n):
    c = 0
    i = 0
    while i * i <= n:
        c = c + 1
        i = i + 1
    return c

if __name__ == '__main__':
    n = 100
    print(f'O(n) - count: {o_n(n)} - n = {n}')
    print(f'O(n**2) - count: {o_n2(n)} - n**2 = {n**2}')
    print(f'O(n ln n) - count: {o_nlogn(n)} - n*math.ln(n) = {n*math.log(n)}')
    print(f'O(sqrt(n)) - count: {o_sqrt_n(n)} - math.sqrt(n) = {math.sqrt(n)}')