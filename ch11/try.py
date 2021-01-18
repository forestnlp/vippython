

try:
    a = input('give a number')
    b = input('give a number')
    a = int(a)
    b = int(b)
    print(a/b)
except ZeroDivisionError as e:
    print('zero',e)
except BaseException as e:
    print(e)
else:
    print("success")
finally:
    print("over finally ")