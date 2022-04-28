from math import inf, gcd
import numpy as np

# def lcm(a, b, c):
#     return abs(a*b*c) // gcd(a, b, c)


def troco(moedas, amount):
    cache = [0] * (amount + 1)
    return 0 if amount < 1 else troco_recursivo(moedas, amount, cache)


def troco_recursivo(moedas, resto, cache):

    if resto < 0:
        return inf

    if resto == 0:
        return 0

    if cache[resto] != 0:
        return cache[resto]

    minimo = inf
    for m in moedas:
        resp_ant = troco_recursivo(moedas, resto - m, cache)

        if (resp_ant >= 0 and resp_ant < minimo):
            minimo = 1 + resp_ant

    cache[resto] = minimo

    # print(cache)
    return cache[resto]


if __name__ == '__main__':
    moedas = [5, 10]
    v = 65
    k = 6
    print("Não") if troco(moedas, v) > k else print("Sim")

    # mmc = mmc(5, 10, 65)
    moedas = [1, 2]
    v = 13
    print("Não") if troco(moedas, v) > k else print("Sim")

    moedas = [5, 10]
    v = 55
    print("Não") if troco(moedas, v) > k else print("Sim")

    # mmc = mmc(5, 10, 55)
    moedas = [1, 2]
    v = 11
    print("Não") if troco(moedas, v) > k else print("Sim")

    moedas = [1, 2, 5]
    amount = 11
    print(troco(moedas, amount))

    moedas = [1, 2, 5]
    amount = 10
    print(troco(moedas, amount))

    moedas = [1, 2, 5]
    amount = 9
    print(troco(moedas, amount))

    moedas = [5, 10]
    amount = 8
    print(troco(moedas, amount))

    a = [5, 10, 55]
    d = gcd(*a)
    print([x / d for x in a])

    a = [5, 10, 65]
    d = gcd(*a)
    print([x / d for x in a])

    a = [1, 2, 3]
    d = gcd(*a)
    print([x / d for x in a])
