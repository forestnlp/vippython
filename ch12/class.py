class Animal:
    # 类属性
    age = 200

    # 初始化方法
    def __init__(selfaaa, name):
        age = 20
        # 覆盖实例属性
        # selfaaa.age=20
        print('init', age)
        selfaaa.name = name

    # 静态方法
    @staticmethod
    def print():
        print("static method called")

    # 类方法
    @classmethod
    def clsprint(cls):
        print("class method called")
        name = 100

    # 实例方法
    def eat(self):
        print("it is eating,instance method")


animal = Animal("aaaa")

# 对象
print(type(Animal))
print(id(Animal))
print(Animal)
print(Animal.age)

Animal.age = 100

# 对象
print(type(animal))
print(id(animal))
print(animal)

# 类属性
print(animal.age)

# 静态方法
Animal.print()

# 类方法
Animal.clsprint()
# 无法更改name属性
print(animal.name)

# Error 类无法调用实例对象
# Animal.eat()
Animal.eat(animal)  # 实例方法
