b = int(input())
a = list()
for i in range(b):
    a.append(input())
a = list(set(a))
a.sort()
a = sorted(a, key= lambda x : len(x))

a = '\n'.join(a)
print(a)