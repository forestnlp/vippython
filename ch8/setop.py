

s = set(range(20))

print(10 in s)

print(98 in s)

print(100 in s)


s.add(100)
print(s)

s.update(range(30))
print(s)

s.update([101,102])
print(s)

s.update((103,104))
print(s)

#此时失效
#s.update(set(105,106))
print(s)

s.remove(100)
print(s)

s.discard(1)
print(s)

s.pop()
print(s)

s.clear()
print(s)

s1 = set((10,20))
s2 = set((20,10))
print(s1 == s2)


