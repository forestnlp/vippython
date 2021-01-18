
class Book:

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def toString(self):
        return str(self.id)+self.name


book1 = Book(1,"莎士比亚之王子复仇记")

print(book1.toString())

book1.price = 200

print(book1.price)

def read():
    print('book reading')

book1.read = read

book1.read()