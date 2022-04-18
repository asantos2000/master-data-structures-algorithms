'''
Find k smallest value on a list
'''
def find_small(V, k):
    # sorting the list
    V.sort()

    # printing the k lowest element
    return V[k-1]

if __name__ == "__main__":
    X = [4, 8, 12, 12, 16]
    Y = [2, 6, 6, 11, 14]
    print(find_small(X + Y, 1))

    assert(find_small(X + Y, 1) == 2)
    assert(find_small(X + Y, 2) == 4)
    assert(find_small(X + Y, 3) == 6)
    assert(find_small(X + Y, 4) == 6)
    assert(find_small(X + Y, 5) == 8)
    assert(find_small(X + Y, 6) == 11)
    assert(find_small(X + Y, 7) == 12)
    assert(find_small(X + Y, 8) == 12)
    assert(find_small(X + Y, 9) == 14)
    assert(find_small(X + Y, 10) == 16)