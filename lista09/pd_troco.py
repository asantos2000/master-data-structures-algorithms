from cmath import inf


def troco(x, k, v):  # sourcery skip: use-contextlib-suppress
    t = [inf] * (v+1)
    t[0] = 0
    M = len(t)

    for i in x:
        #try:
        t[i+1] = 1
        #except IndexError:
        #    pass

    for m in range(1, M):
        for l in range((m//2)+1):
            valor_candidato = t[l] + t[m - l]
            if valor_candidato < t[m]:
                t[m] = valor_candidato
    print(M, m, t[m], k)
    return t[m] <= k # inf se não encontrar solução


if __name__ == '__main__':
    moedas = [0, 5, 10]
    v = 65
    k = 6
    print("Não") if troco(moedas, k, v) else print("Sim")

    moedas = [0, 5, 10]
    v = 55
    k = 6
    print("Não") if troco(moedas, k, v) else print("Sim")
