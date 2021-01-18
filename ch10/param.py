l1 = [1,2,3]
a = 10

def f(l1,a):
    l1.pop()
    a-=1

f(l1,a)

print(l1,a)


def f2(l1,a):
    l1=[1,2,3,4,5]
    a-=1

f2(l1,a)
print(l1,a)

#默认参数

def f3(a=100,b=10):
    return a*b

r = f3(20)
print(r)