#6시 50분 7시 8분
# 골4
n = int(input())
a = list(map(int, input().split()))
n1 = n-1
updp = [0] * (n+1)
dodp = [0] * (n+1)
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and updp[i] < updp[j]:
            updp[i] = updp[j]
        if a[n1-i] > a[n1-j] and dodp[n1-i] < dodp[n1-j]:
            dodp[n1-i] = dodp[n1-j]
    updp[i]+=1
    dodp[n1-i]+=1
maxi = 0
for i in range(len(updp)):
    sum1 = updp[i] + dodp[i] -1
    if maxi < sum1:
        maxi = sum1
print(maxi)