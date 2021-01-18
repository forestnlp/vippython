
s1 = "hello,china"

print(s1.center(20,'*'))

print(s1.ljust(20,'*'))

print(s1.rjust(20,'*'))

print(s1.zfill(20))

for i in range(1,2000):
    string = str(i)
    print(string.rjust(4,'0'))
    print(string.zfill(5))