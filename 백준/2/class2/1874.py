#16시 18분 잠시 쉬엇다가자
#스택 수열 스택의 성질 이용
#시간 초과 n^2의 성질을 갖고있어 10,000,000,000 
import sys
from collections import deque

n = int(input())
vi_map = deque([True]*(n+1))
a = []  #문제 pop 배열들
stack = deque()
stack2 = deque()
answer = ""
for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))
for i in range(len(a)):
    if i == 0 or a[i] >= a[i-1]:
        for j in range(1,a[i]+1):
            if vi_map[j] == True:   
                vi_map[j] = False
                stack2.append("+")
                stack.append(j)
    if stack[-1] == a[i]:
        stack.pop()
        stack2.append("-")
    else:
        answer = "NO"
        break
if len(answer) != 0:
    print(answer)
else:
    for i in stack2:
        print(i)


# n = int(input())
# a = []
# stack = []
# answer = []
# b = [i for i in range(1, n+1)]
# for i in range(n):
#     a.append(int(sys.stdin.readline()))

# for i in range(len(a)):
#     if i == 0:
#         for j in range(a[i]):
#             stack.append()
#             answer.append("+")
#         stack.pop()
#         answer.append("-")
#     elif a[i] > a[i-1]:
#         for j in range(a[i] - a[-1]):
#             stack.append(b.pop(0))
#             answer.append("+")
#         stack.pop()
#         answer.append("-")
#     elif a[i] < a[-1]:
#         stack.pop()
#         answer.append("-")
# print(answer)