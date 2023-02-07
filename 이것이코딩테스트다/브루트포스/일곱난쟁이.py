a = []
for i in range(9):
    a.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        result = sum(a) - a[i] - a[j]
        if result == 100:
            a.pop(j)
            a.pop(i)
            break
    if len(a) == 7:
        break
a.sort()
for i in range(7):
    print(a[i])
print(sum(a))
