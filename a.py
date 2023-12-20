def fun(a,b):
    a = a + 4
    b.append(5)
    return (a,b)

a = 1
b = []
print(fun(a,b))
print(a)