#10시 41분 10시 45분

a = input().split()

for i in range(len(a)):
    a[i] = a[i][::-1]
if int(a[0]) >= int(a[1]):
    print(a[0])
else:
    print(a[1])