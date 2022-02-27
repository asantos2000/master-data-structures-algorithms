# c ← 1
# para (i = 1; i ≤ n;i + +) faça
#     para (j = 1; j ≤ n; j = j + i) faça
#         imprime(c)
#         c ← c + 1

def loop_count(n):
#n = 1
    c = 1
    for i in range(1, n+1):
        j = 1
        while j <= n:
            #print(i, j, i + j, n, n <= j)
            #print(n, c)
            c = c + 1
            j = j + i
    return c-1

if __name__ == "__main__":
    for n in range (1, 1001):
        c = loop_count(n)
        print(f'{n};{c}')
    #print(loop_count(10))