'''
Busca binária iterativa
Exercício: Lista 1.1

Requerido: python 3+, pip install -r requirements.txt
Executar: python busca_binaria.py
'''

def binarySearch(arr, x):
  
    l, r = 0, len(arr)-1
    while l <= r:
        mid = l + (r - l) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # If x is smaller, ignore right half
        else:
            r = mid - 1
  
    # If we reach here, then the element
    # was not present
    return -1

if __name__ == "__main__":
    assert(binarySearch([1, 2, 3, 4, 5, 6], 4) == 3)
    assert(binarySearch([1, 2, 3, 4, 5, 6], 1) == 0)
    assert(binarySearch([1, 2, 3, 4, 5, 6], 6) == 5)
    assert(binarySearch([23, 32, 44, 45, 45, 60], 44) == 2)
    assert(binarySearch([23, 32, 44, 45, 45, 60], 45) == 3)
    assert(binarySearch([23, 32, 44, 45, 45, 60], 100) == -1)
    assert(binarySearch([23, 32, 44, 45, 45, 60], 23) == 0)
    assert(binarySearch([23, 32, 44, 45, 45, 60], 60) == 5)
    assert(binarySearch([23, 32, 44, 45, 45, 60], 32) == 1)
    assert(binarySearch([0, 0], 0) == 0)
