#6시58분 7시 20분
# 실4
from collections import deque as de
n, k = map(int, input().split())
a = de([i for i in range(1, n+1)])
answer = de()
while len(answer) != n:
    for i in range(k-1):
        a.append(a.popleft())
    num = a.popleft()
    answer.append(num)
print('<',", ".join(map(str, answer)), '>', sep='')
