# 3시51분 4시
# 브1
import math
import sys
input = sys.stdin.readline
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     c = math.gcd(a, b)
#     print(int(a * b / c))


def gcd(num1, num2):
    if num1 < num2:
        return num1
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    big = max(a, b)
    small = min(a, b)
    print(big*small/gcd(big, small))
