class Person:
    def __new__(cls, *args, **kwargs):
        print("at new method,cls=:", id(cls))
        obj = super().__new__(cls)  # object construct
        print("at new method,obj=", id(obj))
        return obj

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('liujie',36)

print(id(p))