s = {1,2,3,4,5,6,7,8,9,"Paras"}
print(s, type(s))

s.add(27)
print(s, type(s))
s.remove(2)
print(s, type(s))

s1 = {1,2,3,4,5}

s2 = {6,5,4,2,9}

print(s1.union(s2))
print(s1.intersection(s2))
