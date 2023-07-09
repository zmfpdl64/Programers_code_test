# 20시 13분
# 20시 35분
# https://www.acmicpc.net/problem/6986
# Round-to-nearest-even 이건 앞자리가 짝수냐 홀수냐에 따라 반올림이 되고 안되고 함
# 통계학에서 비롯됨
# https://blog.naver.com/noseoul1/221592047071
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = [float(input()) for _ in range(n)]
a.sort()
b = a[k:n-k]
c = a[:k]+a[n-k:]
for i in range(len(c)):
    mini = float('inf')
    left = 0
    right = len(b) - 1
    mid = (left+right) // 2
    while left <= right:
        mid = (left+right) // 2
        diff = c[i] - b[mid]
        if diff < 0:
            right = mid - 1
        elif diff > 0:
            left = mid + 1
        else:
            break
    c[i] = b[mid]
a_avg = (sum(b)/len(b))
b_avg = (sum(b)+sum(c)) / (len(b)+len(c))
def roundValue(value):
    value *= 1000
    mod = value % 10
    if mod >= 5:
        value -= mod
        value += 10
        return value / 1000
    return (value-mod) / 1000
print(f"{roundValue(a_avg):.2f}")
print(f"{roundValue(b_avg):.2f}")