# 20시 22분 20시 43분
# 실3
n = int(input())
a = list(map(int, input().split()))
for i in range(len(a)-1, 0, -1):
    if a[i] < a[i-1]:
        for j in range(n-1, 0  , -1):
            if a[i-1] > a[j]:
                a[i-1], a[j] = a[j], a[i-1]
                a[i:] = sorted(a[i:], reverse = True)
                print(*a)
                exit()
print(-1)