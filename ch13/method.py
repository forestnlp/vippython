
class Student:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("merry")
stu2 = Student("me")

# __add__
print(stu1+stu2)

print(len(stu1))
