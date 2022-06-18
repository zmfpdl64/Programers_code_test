a = input()

b = {i : -1 for i in "abcdefghijklmnopqrstuvwxyz"}
b = dict(sorted(b.items(), key = lambda x : x[0]))

for i in range(len(a)):
    if b[a[i]] >= 0:
        pass
    else:
        b[a[i]] = i
c = list(b.values())
print(c)