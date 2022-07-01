#16시 18분 잠시 쉬엇다가자
#스택 수열 스택의 성질 이용

import sys


n = int(input())
a = []
stack = []
answer = []
b = [i for i in range(1, n+1)]
for i in range(n):
    a.append(int(sys.stdin.readline()))

for i in range(len(a)):
    if i == 0:
        for j in range(a[i]):
            stack.append()
            answer.append("+")
        stack.pop()
        answer.append("-")
    elif a[i] > a[i-1]:
        for j in range(a[i] - a[-1]):
            stack.append(b.pop(0))
            answer.append("+")
        stack.pop()
        answer.append("-")
    elif a[i] < a[-1]:
        stack.pop()
        answer.append("-")
print(answer)