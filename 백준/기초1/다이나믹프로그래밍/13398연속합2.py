# 7시32분
# 골5

n = int(input())
a = [-1000] + list(map(int, input().split()))
adp = a.copy()
bdp = a.copy()
for i in range(1, n+1):
    adp[i] = max(adp[i-1] + a[i], adp[i])
    bdp[i] = max(adp[i-1], a[i] + bdp[i-1])
print(adp)
print(bdp)
print(max(max(adp), max(bdp)))