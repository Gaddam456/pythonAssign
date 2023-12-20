a = 2
b = 5

def add(a,b):
    c = a + b
    d = c - 1
    list_a = [c, d]
    return list_a

addition1 = add(a,b) # list_a
addition2 = add(23,20) # list_a

print(addition1[0]+1000)
print(addition2[0]+200)