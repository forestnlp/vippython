dic1 = {3:1,'b':3}

dic2 = dict(name="liujie",age=35)

print(dic1[3])

for item in dic1:
    print(item)

print(dic2['name'],dic2['age'],dic2.get("gender","male"))