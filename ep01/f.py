from math import sqrt
import re


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# fibonacci O(n)
# T(n) = T(n-1) + T(n-2) + O(1) = O(2^n)
# https://www.educative.io/courses/algorithms-coding-interviews-java/xV634O2M8Ml
def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

# fibonacci O(n)
def f_p(n):
    stack = []
    result = 0
    for i in range(n+1):
        stack.append(i)

    while len(stack) > 0:
        result = result + stack.pop()

    return result

# fibonacci O(1)
# https://www.geeksforgeeks.org/time-complexity-recursive-fibonacci-program/
def f_p_1(n):
    return round(
        ((1+sqrt(5))**n - (1-sqrt(5))**n) / (2**n*sqrt(5))
        )


if __name__ == "__main__":
    print(fibonacci(10))
    print(f(10))
    print(f_p(10))
    print(f_p_1(10))
