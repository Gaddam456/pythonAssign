import functools as f
list_a = [1,2,3,5,4]
print(f.reduce(lambda a,b: a if a>b else b, list_a))
print(f.reduce(lambda a,b: a+b, list_a))
print(f.reduce(lambda a,b: b-a, list_a))
print(f.reduce(lambda a,b: a*b, list_a))