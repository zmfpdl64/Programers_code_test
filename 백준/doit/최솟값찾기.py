# 15시 38분
# 플5
# https://www.acmicpc.net/problem/11003
from collections import deque
n, l = map(int, input().split())
a = list(map(int , input().split()))
dq = deque()
ans = []
# dq 순서, 값
for i, v in enumerate(a):
    while dq and dq[-1][1] >= v:
        dq.pop()
    dq.append((i, v))
    if dq[0][0] <= i - l:
        dq.popleft()
    ans.append(dq[0][1])
print(*ans)