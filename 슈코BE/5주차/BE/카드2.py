# 16시 18분 16시 30분
# 실4
# https://www.acmicpc.net/problem/2164
from collections import deque
# 시간 제한 2초
# 1 <= N <= 500_000 파이썬의 list를 그냥 사용하면 시간초과 발생할 수 있음 n^2

n = int(input())
queue = deque([i for i in range(1, n+1)])
while(len(queue) != 1):
    # 1, 2, 3, 4, 5, 6
    queue.popleft()
    # 2, 3, 4, 5, 6
    queue.rotate(-1)
print(queue[0])


class Node:

    next
    def __init__(self, prev, next):
        self.prev = prev
        self.next = next
