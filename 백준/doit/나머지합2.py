import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = 0
a = [0] * m
for i in range(n):
    ans += num[i]
    a[ans%m] += 1
result = a[0]
for i in a:
    result += i*(i-1)//2
print(result)
