
file = open('aaa','a')
file.write("abcde")
file.write("dasd\n")
file.write("grerga")
file.close()

file = open('aaa','r')
str = file.readlines()
print(str)
file.close()