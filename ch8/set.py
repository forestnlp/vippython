
set1 = {1,2,3,3,4,5,1}

print(set1)


for i in range(10):
    set1.add(i)
print(set1)


set2 = set({1,2,3,4,4,2,2,1})
print(type(set2),set2)

set3 = set(range(5))
print(set3,type(set3))

set4 = set([1,2,3,4,1,123,2,3])
print(set4,type(set4))

set5 = set((1,2,3,4,1,123,2,3))
print(set5,type(set5))

#定义空集合的方法，需要与字典进行区分

a = {} #空字典
b = set() #空集合


c = {i*i for i in range(100)}
print(c)