import math

def bpp_pi():
    from decimal import Decimal, getcontext
    getcontext().prec=100
    return sum(1/Decimal(16)**k * 
            (Decimal(4)/(8*k+1) - 
            Decimal(2)/(8*k+4) - 
            Decimal(1)/(8*k+5) -
            Decimal(1)/(8*k+6)) for k in range(100))

def wallis(n):
    pi = 2
    for i in range(1,n):
        pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
    return pi

if __name__ == "__main__":
    pi = wallis(100000)
    s = f"Wallis π is approximately {pi:.15f}"
    print(s)
    print(f"Python math.pi is {math.pi}")
    print(f"Bailey-Borwein-Plouffe π is {bpp_pi():.15f}")
