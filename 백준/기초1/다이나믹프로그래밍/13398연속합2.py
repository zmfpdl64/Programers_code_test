# 7시32분
# 골5

n = int(input())
a = list(map(int, input().split()))
adp = a.copy()
bdp = a.copy()
for i in range(1, n):
    adp[i] = max(adp[i-1] + a[i], a[i])
    bdp[i] = max(bdp[i-1] + a[i], adp[i-1])
print(adp)
print(bdp)
print(max(max(adp), max(bdp)))