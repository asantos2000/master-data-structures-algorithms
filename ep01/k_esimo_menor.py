'''
kEsimoMenor (X, Y, lx, rx, ly, ry, k)
se (lx > rx) então
	retorna Y [ly + k - 1]
se (ly > ry) então
	retorna X[lx + k - 1]

midx ← (lx + rx)/2
midy ← (ly + ry)/2
nx ← midx - lx + 1
ny ← midy - ly + 1

se (nx + ny > k) então
	se (X[midx] > Y [midy]) então
		retorna kEsimoMenor (X, Y , lx, midx - 1, ly, ry, k)
	senão
		retorna kEsimoMenor (X, Y , lx, rx, ly, midy - 1, k)
senão
	se (X[midx] > Y [midy]) então
		retorna kEsimoMenor (X, Y , lx, rx, midy + 1, ry, k - ny)
	senão
		retorna kEsimoMenor (X, Y , midx + 1, rx, ly, ry, k - nx)
'''


def k_esimo_menor(X, Y, lx, rx, ly, ry, k):
    # print(f'{len(X+Y)}; {1}') # Descomentar para pytest -s > result_count.txt
    if (lx > rx):
        return Y[ly + k - 1]
    if (ly > ry):
        return X[lx + k - 1]

    midx = (lx + rx) // 2
    midy = (ly + ry) // 2
    nx = midx - lx + 1
    ny = midy - ly + 1

    if (nx + ny > k):
        if (X[midx] > Y[midy]):
            return k_esimo_menor(X, Y, lx, midx - 1, ly, ry, k)
        else:
            return k_esimo_menor(X, Y, lx, rx, ly, midy - 1, k)
    else:
        if (X[midx] > Y[midy]):
            return k_esimo_menor(X, Y, lx, rx, midy + 1, ry, k - ny)
        else:
            return k_esimo_menor(X, Y, midx + 1, rx, ly, ry, k - nx)


if __name__ == "__main__":
    # Case 1
    X = [4, 8, 12, 12, 16]
    Y = [2, 6, 6, 11, 14]
    lx = 0
    rx = len(X)-1
    ly = 0
    ry = len(Y)-1

    print(k_esimo_menor(X, Y, lx, rx, ly, ry, 2))

    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 1) == 2)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 2) == 4)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 3) == 6)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 4) == 6)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 5) == 8)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 6) == 11)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 7) == 12)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 8) == 12)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 9) == 14)
    assert(k_esimo_menor(X, Y, lx, rx, ly, ry, 10) == 16)
