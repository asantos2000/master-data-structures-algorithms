def quad(a: int) -> int:
    return a**2

def area(a: int, b: int) -> int:
    if a > 0 and b > 0:
        return quad(b) + area(a-b, b) if a > b else quad(a) + area(a, b-a)
    else:
        return 0

if __name__ == '__main__':
    assert(area(4, 2)==8)
    assert(area(3, 5)==15)
    assert(area(13, 5)==65)
    assert(area(13, 8)==104)
    assert(area(13, 10)==130)
    assert(area(1, 1)==1)
    assert(area(2, 2)==4)
    assert(area(0, 0)==0)
    assert(area(0, 1)==0)
    assert(area(1, 0)==0)
    