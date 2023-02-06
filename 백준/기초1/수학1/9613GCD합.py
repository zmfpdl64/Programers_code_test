#1시 17분 1시 40분
# 실4
import sys
input = sys.stdin.readline
n = int(input())

def gcd(num1, num2):
    if num1 < num2:
        return num1
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)
for i in range(n):
    a = list(map(int, input().split()))
    a = a[1:]
    a.sort()
    answer = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            answer.append(gcd(a[j], a[i]))
    print(sum(answer))

