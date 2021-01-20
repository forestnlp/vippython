class ClassA:
    def __init__(self, id):
        self.id = id

    def message(self):
        print('my id is ', self.id)


class Class0:
    def message0(self):
        print("class0 message0")


class ClassB(ClassA, Class0):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def message0(self):
        # super().message0()
        print("classB message0", self.name)

    def __str__(self):
        # return "我的信息是 :"+str(type(self))+",id="+str(self.id)+",name="+self.name
        return "我的信息是id：{0},name:{1}".format(self.id,self.name)

b = ClassB(1, 'bbbb')
b.message()
b.message0()

print(dir(b))

print(b.__str__())