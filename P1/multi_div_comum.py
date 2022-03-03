def mdc_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mdc_recursivo(b, a % b)

def mdc_iterativo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mmc_iterativo(a, b):
   if a > b:
       maior = a
   else:
       maior = b

   while(True):
       if ((maior % a == 0) and (maior % b == 0)):
           mmc = maior
           break
       maior += 1

   return mmc

if __name__ == "__main__":
    print(mdc_recursivo(12, 8))
    print(mdc_iterativo(12, 8))
    print(mdc_iterativo(12, 83))
    print(mdc_iterativo(2, 3))
    print(mmc_iterativo(12, 8))
    print(mmc_iterativo(12, 83))
    print(mmc_iterativo(2, 3))