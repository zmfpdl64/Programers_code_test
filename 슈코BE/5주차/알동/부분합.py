# 14시 15분 14시 35분
# 골4
# https://www.acmicpc.net/problem/1806

n, m = map(int, input().split())
ins = list(map(int, input().split()))
start = 0
end = 0
sum1 = ins[0]
mini = float('INF')

while end < n:
    if sum1 >= m:
        mini = min(mini, end-start+1)
        sum1 -= ins[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        sum1 += ins[end]
if mini == float('inf'):
    print(0)
else:
    print(mini)