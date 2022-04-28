def outer():
    a = 10
    def inner():
        print(a)
    return inner

res = outer()
res()
# 10