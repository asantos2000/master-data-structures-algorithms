'''
maxMin (v[0..n − 1], n) 
1 max ← v[0] 
2 min ← v[0] 
3 para (i = 1; i < n; i++) faça 
4	se (v[i] > max) então 
5		max ← v[i] 
6	se (v[i] < min) então
7		min ← v[i]
'''

from hypothesis import given, event, strategies as st

def max_min(V):  # sourcery skip: avoid-builtin-shadow
    max = V[0]
    min = V[0]
    for i in range(len(V)):
        if V[i] > max:
            max = V[i]
        if V[i] < min:
            min = V[i]
    return min, max

if __name__ == "__main__":
    print(max_min([1,2,3,4,5,8,9,10]))
    print(max_min([5,2,3,4,12,8,9,0]))

@given(st.lists(st.integers(), min_size=1))
def test_max_min(xs):
    lst_min = min(xs)
    lst_max = max(xs)
    event(f'{xs}, {lst_min}, {lst_max}')
    assert(max_min(xs) == (lst_min,lst_max))