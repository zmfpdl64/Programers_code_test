#1시41분 2시 25분
# 실2


def gcd(num1, num2):
    if num1 < num2:
        return num1
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)
import sys
input = sys.stdin.readline

n, pos = map(int, input().split())
a = list(map(int, input().split()))
dif = []
for i in range(len(a)):
    dif.append(abs(pos-a[i]))
num = dif[0]
for i in range(len(dif)):
    b = max(num, dif[i])
    s = min(num, dif[i])
    num = gcd(b, s)
print(num)