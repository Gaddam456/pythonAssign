def bubbleSort(a):
    for i in range(len(a)): # i --> 0, 1, 2, 3
        for j in range(0,len(a)-i-1): # i --> 2 range(0, 1) j --> 0
            if a[j]>a[j+1]: # 4 > 2
                a[j], a[j+1] = a[j+1], a[j] # [2, 4, 5, 7]
a = [7,4,5,2]
bubbleSort(a)
print(a)
b = [7,4,5,2]

print(sorted(b))
