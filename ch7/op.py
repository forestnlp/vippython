
dic = {"name":"liujie","age":35,"gender":"male"}

for item in dic.items():
    print(item)

for key in dic.keys():
    print(key)

for val in dic.values():
    print(val)

for k,v in dic.items():
    print(k,v)

print(type(dic.items()),type(dic.keys()),type(dic.values()))