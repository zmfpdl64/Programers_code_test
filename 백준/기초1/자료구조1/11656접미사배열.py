#3시 32분 3시 34분
#실4
str1 = input()
a = []
for i in range(len(str1)):
    a.append(str1[i:])
a = sorted(a)
for i in a:
    print(i)