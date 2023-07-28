map1 = {}
n = int(input())
for i in range(n):
    str1, str2 = map(list, input().split())
    if str1 not in map1:
        map1[str1] = 1
    else:
        map1[str1] +=1
    if str2 not in map1:
        map1[str2] = 1
    else:
        map1[str2] += 1
for value in map1.values():
    if value != 2:
        print("Impossible")
        break
else:
    print("Possible")