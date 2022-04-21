def mdc_recursivo(a, b):
    return a if b == 0 else mdc_recursivo(b, a % b)

def mdc_iterativo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mmc_iterativo(a, b):
    maior = a if a > b else b
    while(True):
        if ((maior % a == 0) and (maior % b == 0)):
            mmc = maior
            break
        maior += 1

    return mmc

if __name__ == "__main__":
    print(mdc_recursivo(12, 8))
    print(f'mdc(12,8) = {mdc_recursivo(12,8)}')
    print(f'mdc(8,12) = {mdc_recursivo(8,12)}')
    print(f'mdc(92,72) = {mdc_recursivo(92,72)}')
    print(f'mdc(92-72,72) = {mdc_recursivo(92-72,72)}')
    print(f'mdc(5,5) = {mdc_recursivo(5,5)}')
    print(f'mdc(0,12) = {mdc_recursivo(0,12)}')
    print(f'mdc(8,0) = {mdc_recursivo(8,0)}')
    print(f'mdc(0,0) = {mdc_recursivo(0,0)}')
   
    print(mdc_iterativo(12, 8))
    print(mdc_iterativo(12, 83))
    print(mdc_iterativo(2, 3))
    print(mmc_iterativo(12, 8))
    print(mmc_iterativo(12, 83))
    print(mmc_iterativo(2, 3))