
a = "hello"
b = 'hello'
c = '''hello'''

print(id(a))
print(id(b))
print(id(c))

a = 'x%'
b = 'x%'
#pycharm优化
print(a==b,a is b)

#字符串的驻留机制

#如果包含特殊字符不会驻留。可以强制system.intern方法来驻留

s1 = 'hello'
print(s1.upper())
print(s1.capitalize())
print(s1.capitalize().swapcase())

s2 = "hello,china"
print(s2.title())


print('hello'.index('l'))
print('hello'.rindex('l'))
print('hello'.find('a'))
print('hello'.rfind('a'))
