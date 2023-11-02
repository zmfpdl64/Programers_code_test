# 14시 10분
# 골 3
# https://www.acmicpc.net/problem/1005
# T
# 건물의 갯수 2 <= N <= 1000
# 건설순서 1<= K <= 100,000
# 각 건물당 걸리는 시간 0 <= D <= 100,000
# 1 <= X, Y  x다음 y건물 구축 가능

import sys
from collections import deque
input = sys.stdin.readline

def getMinTime(start, graph, times, dp):
    q = deque([start])
    maxi = dp[start]
    vi_map = [False] * len(dp)
    while q:
        cur = q.popleft()
        for nex in graph[cur]:
            time = times[nex]
            total_time = time + dp[cur]
            if total_time > dp[nex] or (not vi_map[nex] and times[nex] == dp[nex]):
                dp[nex] = total_time
                vi_map[nex] = True
                maxi = max(total_time, maxi)
                q.append(nex)
    return maxi
def solution():
    n, k = map(int, input().split())
    graph = {i : [] for i in range(1, n+1)}
    delay = [0] + list(map(int, input().split()))
    dp = delay[::]

    for i in range(k):
        x, y = map(int, input().split())
        graph[y].append(x)
    start = int(input())
    maxi = getMinTime(start, graph, delay, dp)
    print(maxi)

t = int(input())
for i in range(t):
    solution()

