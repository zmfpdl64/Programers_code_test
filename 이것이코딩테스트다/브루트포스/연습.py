from itertools import combinations as cb
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

d = [a, b, c]
e = zip(a,b)
f = [sum(i) + sum(j) for i, j in zip(d, zip(*d))]
g = list(zip(d, zip(*d)))
h = sum(a) + sum(b) + sum(c)
l = sum(f)
print(*e)
print(zip(a, b))
for i, j in zip(d, zip(*d)):
    print(i, j)
print(f)
print(g)
print(h)
print(h // 2)
min_v = 100000
for i in cb(f[::-1], 3):
    min_v = min(min_v, abs(l - sum(i)))
    print(min_v)
print(l)
