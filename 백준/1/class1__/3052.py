#10시 34분 10시 38분
#나머지 문제

a = list()
b = list()
# a = list(map(int, input().split()))
for i in range(10):
    a.append(int(input()))

for i in range(len(a)):
    b.append(a[i] % 42)
num = list(set(b))
print(len(num))
