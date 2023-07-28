# 20시 33분 20시 50분
# 실4
# https://www.acmicpc.net/problem/1158
from collections import deque

def solution2():
    n, k = map(int, input().split())
    ans = []
    stack = list(range(1, n+1))
    idx = 0
    while stack:
        idx += k-1
        idx %= len(stack)
        ans.append(stack.pop(idx))
    print('<', ', '.join(map(str, ans)), '>', sep='')
solution2()


def solution1():
    n, k = map(int, input().split())
    ans = []
    queue = deque(range(1, n+1))
    while queue:
        queue.rotate(-(k-1))
        ans.append(queue.popleft())
    print('<' ,', '.join(map(str, ans)), '>', sep='')

