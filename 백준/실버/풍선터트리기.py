# 20시 38분 나중에 풀기
# https://www.acmicpc.net/problem/2346
from collections import deque
n = int(input())
ins = deque(enumerate(map(int, input().split(" ")), start=1))
answer = []
for i in range(n):
    a = ins.popleft()
    print(a[0], end=' ')
    if a[1] > 0:
        ins.rotate(-(a[1]-1))
    else:
        ins.rotate(-(a[1]))


