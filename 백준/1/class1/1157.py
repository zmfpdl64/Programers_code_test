a = input()
a = a.lower()

dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
key = sorted(dic.items(), key = lambda x : x[1])
print(key)
