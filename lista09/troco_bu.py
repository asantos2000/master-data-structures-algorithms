from cmath import inf


def troco(moedas, v):
    a = [inf] * (v+1)
    a[0] = 0

    for i in range(1, len(a)):
        for m in moedas:
            if m <= i:
                a[i] = min(a[i], a[i-m] + 1)
            else:
                a[i]
    #print(a)
    return a[i] # inf se não encontrar solução


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
    v = 11
    print(troco(moedas, v))

    moedas = [1, 2, 5]
    v = 10
    print(troco(moedas, v))

    moedas = [1, 2, 5]
    v = 9
    print(troco(moedas, v))

    moedas = [5, 10]
    v = 8
    print(troco(moedas, v))