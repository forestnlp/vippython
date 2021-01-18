

s1 = {1,2,3}
s2 = {2,3,4,5}
s3 = {1,2,3,4,5}
s4 = {1,2,3,4,5,6}

print(s1.issubset(s3)) #true
print(s3.issubset(s4)) #true

print(s3.issuperset(s1)) #true
print(s4.issuperset(s3)) #true

print(s1.isdisjoint(s2)) #false

print(s1.intersection(s2))
print('&',s1&s2)

print(s1.union(s2))
print(s1|s2)

print(s1-s2)
print(s1.difference(s2))

print(s1.symmetric_difference(s2))
print(s1^s2)