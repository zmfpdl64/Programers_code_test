import heapq
n, m = map(int, input().split())
dp = [100_001] * 100_001
queue = [[0, n]]
if n == m :
    print(0)
    exit()
while queue:
    t, cur = heapq.heappop(queue)
    move = [cur+1, cur-1, cur*2]
    for nex in move:
        if 0 <= nex <= 100_000 and dp[nex] > t+1:
            dp[nex] = t+1
            heapq.heappush(queue, [t+1, nex])

print(dp[m])