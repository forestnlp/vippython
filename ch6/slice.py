
list1 = [i for i in range(40)]

print(list1)

print(list1[5:20])

print(list1[5:20:3])

print(list1[::3])

print(list1[::5])

print(list1[::-5])

slicelist = list1[5:20:3];

print(id(slicelist),id(list1))