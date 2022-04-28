# https://medium.com/geekculture/4-steps-to-do-algebra-with-python-3601fe306182
# !pip3 install SymPy

from sympy import Symbol, factor, symbols

a = Symbol('x')
b = Symbol('y')
print(a + a + 1)
# 2*x + 1
print(2*a+a*a+a)
# x**2 + 3*x
print(a*a+3*a+b)
# x**2 + 3*x + y

x,y,z = symbols('x,y,z')
square = x**2 - 2*x*y + y**2
res = factor(square)
print(res)
# (x - y)**2

from sympy import *
x = Symbol('x')
y = Symbol('y')
expr = (x + y) * (x - y)
print(expr)
# (x - y)*(x + y)

res = expand(expr)
print(res)
# x**2 - y**2

x = Symbol('x')
y = Symbol('y')
expr = (x**2 - y**2)/(x + y)

res = simplify(expr)
print(res)
# x - y

expr = x**3 + x*y - x**2 - 2*y + y**3
res = expr.subs({x:1, y:2})
print(res)
# 6

expr = x
res = expr.subs({x:x-1})
print(res)
# x - 1

x,a,b,c=symbols('x,a,b,c')
expr = a*x*x + b*x + c
res = solve(expr, x, dict=True)
print(res)
# [{x: (-b - sqrt(-4*a*c + b**2))/(2*a)}, {x: (-b + sqrt(-4*a*c + b**2))/(2*a)}]

x,y=symbols('x,y')
eq1 = 2*x + 5*y - 6
eq2 = 3*x + 7*y - 12
res = solve((eq1, eq2))
print(res)
# {x: 18, y: -6}

x,y=symbols('x,y')
eq1 = 2*x**2 + 5*x*y - 6
eq2 = 3*x**2 + 7*x*y - 12
res = solve((eq1, eq2))
print(res)
# [{x: -3*sqrt(2), y: sqrt(2)}, {x: 3*sqrt(2), y: -sqrt(2)}]