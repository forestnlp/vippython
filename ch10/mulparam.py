
def f1(*args):
    for a in args:
        print(a)


f1(3,3,1,5,6,7,1)

def f2(**args):
    # print(args)
    for item in args.items():
        print(item)

f2(name='liujie',age=10)

#error
# def f3(**args0,*args1):
def f3(*args1,**args0):
    # print(args)
    for item in args0.items():
        print(item)
    for item in args1:
        print(item)

f3(1,2,3,4,name='liujie')

a = [1,2,3,4]

f3(*a)
f3(a)#没有解包


def f4(*args):
    for _ in args:
        print(_)

f4(*a)
f4(a)

def f5(**args):
    for _ in args:
        print(_)

dic = {'a':1,'b':2}
f5(**dic)
# error
# f5(dic)

#只能使用关键字传递
def f6(a,b,*,c,d):
    pass

#error
# f6(1,2,3,4)

f6(1,2,c=3,d=4)