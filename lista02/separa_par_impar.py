def par(n):
    return n % 2 == 0

def separa_par_impar(V):
    i = 0
    j = 1
    while (i < len(V)) and (j < len(V)):
        if par(V[i]):
            i = i + 1
            j = i + 1
        else:
            if par(V[j]):
                V[i], V[j] = V[j], V[i]
                i = i + 1
            j = j + 1

if __name__ == '__main__':
    V = [1,2,3,4,5]
    separa_par_impar(V)
    print(V)

    V = [2, 4, 3, 1, 5]
    separa_par_impar(V)
    print(V)

    V = [5, 4, 3, 2, 1]
    separa_par_impar(V)
    print(V)

    V = [3,3,3,3,3]
    separa_par_impar(V)
    print(V)

    V = [2,2,2,2,2]
    separa_par_impar(V)
    print(V)

    V = [1,2,1,2,1]
    separa_par_impar(V)
    print(V)

    V = [2,1,2,1,2]
    separa_par_impar(V)
    print(V)

    V = [2,1]
    separa_par_impar(V)
    print(V)

    V = [1,2]
    separa_par_impar(V)
    print(V)

    V = [1]
    separa_par_impar(V)
    print(V)

    V = [4,4,3,1,9,2]
    separa_par_impar(V)
    print(V)