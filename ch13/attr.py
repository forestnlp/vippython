
#print(dir(object))

class A:
    pass

class B:
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

c = C('jack',20)
print(c.__dict__)
print(C.__dict__)


print(c.__class__) #对象所属类型
print(type(c))
print(C.__bases__) #所属所有父类
print(C.__base__) #所属直属父类

print(C.__mro__) #类的层次结构 ，所有上级

print(A.__subclasses__()) #类的所有子类

print(object.__subclasses__())
