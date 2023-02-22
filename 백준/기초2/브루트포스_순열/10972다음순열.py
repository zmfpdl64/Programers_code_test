#18시
# 실3
n = int(input())-1
a = list(map(int, input().split()))
x, y = 0, 0
dif = 0
for i in range(n, 0, -1):
    if a[i] > a[i-1]:
        minv = 10_000
        for j in range(i-1, n+1):
            if a[i-1] < a[j] and minv > a[j]-a[i-1]:
                minv = a[j]-a[i-1]
                x= i-1
                y = j
        a[x],a[y] = a[y],a[x]
        a[x+1:] = sorted(a[x+1:])
        print(*a)
        exit()
print(-1)
