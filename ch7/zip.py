
k = [1,2,3,4]
v = [10,20,30,40]

d = {k0:v0 for k0,v0 in zip(k,v)}
print(d)

d[1]=11

print(d)

print(1 in d)