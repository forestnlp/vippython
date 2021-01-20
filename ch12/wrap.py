

class ClassA:
    #类属性
    attr1 = 10

    #构造方法
    def __init__(self):
        self.attr2 = 20
        #私有属性
        self.__attr3=30

    def print(self):
        print(self.__attr3)

classA = ClassA()

print(classA.attr2)

classA.print()

# print(classA.__attr3)

print(dir(classA))

print(classA._ClassA__attr3)