

class Animal:
    def eat(self):
        print("animal eating")

class Dog(Animal):
    def eat(self):
        print("dog eating meat")

class Cat(Animal):
    def eat(self):
        print("cat eating fish")

class Person(object):
    def eat(self):
        print("person eating corn")
    def drink(self):
        pass

#只关心这个animal对象是否具有eat方法
def fn(animal):
    animal.eat()
    animal.drink()

fn(Person())

fn(Cat())