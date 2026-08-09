lis = [2,4,5,6,7]
lis.append(1)
n = len(lis)
for index, element in enumerate(lis):
    if 1 < element:
        lis.insert(index , 1)
        break
del lis[n]


print(lis)
