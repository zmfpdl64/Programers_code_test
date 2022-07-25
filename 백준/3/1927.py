#14시 54분 15시 07분 잠시 중단
# 1초 128MB 0 <= x < x**31
import collections
import heapq
import sys

input = sys.stdin.readline

t = int(input())

q = list()

answer = []
for i in range(t):
    n = int(input())
    if n != 0:
        heapq.heappush(q, n)
    else:
        if len(q) != 0:
            answer.append(heapq.heappop(q))
        else:
            answer.append(0)

for i in answer:
    print(i)
        