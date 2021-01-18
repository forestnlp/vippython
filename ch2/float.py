
a = 3.14159

print(type(a))

a = 3.1
b = 2.2

print(a+b)

from decimal import Decimal

print(Decimal('3.1')+Decimal('2.2'))

#存在问题
print(Decimal(3.1)+Decimal(2.2))