#10시 45분 10시 55분 성공
a = list(map(int, input().split()))

if a[1] >= 45:
    a[1] -= 45
elif a[1] < 45 and a[0] == 0:
    a[0] = 23
    a[1] = 60 - (45-a[1])
else:
    a[0] -= 1
    a[1] = 60 - (45-a[1])

print('{0} {1}'.format(a[0], a[1]))
