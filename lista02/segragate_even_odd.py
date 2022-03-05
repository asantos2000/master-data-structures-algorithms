'''
Algorithm: segregateEvenOdd()
1) Initialize two index variables left and right: left = 0, right = size -1
2) Keep incrementing left index until we see an odd number.
3) Keep decrementing right index until we see an even number.
4) If left < right then swap arr[left] and arr[right]
'''


def segregateEvenOdd(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1
        while left < right and arr[right] % 2 == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]


if __name__ == '__main__':
    V = [1, 2, 3, 4, 5]
    segregateEvenOdd(V)
    print(V)

    V = [2, 4, 3, 1, 5]
    segregateEvenOdd(V)
    print(V)

    V = [5, 4, 3, 2, 1]
    segregateEvenOdd(V)
    print(V)

    V = [3, 3, 3, 3, 3]
    segregateEvenOdd(V)
    print(V)

    V = [2, 2, 2, 2, 2]
    segregateEvenOdd(V)
    print(V)

    V = [1, 2, 1, 2, 1]
    segregateEvenOdd(V)
    print(V)

    V = [2, 1, 2, 1, 2]
    segregateEvenOdd(V)
    print(V)

    V = [2, 1]
    segregateEvenOdd(V)
    print(V)

    V = [1, 2]
    segregateEvenOdd(V)
    print(V)

    V = [1]
    segregateEvenOdd(V)
    print(V)

    V = [4, 4, 3, 1, 9, 2]
    segregateEvenOdd(V)
    print(V)
