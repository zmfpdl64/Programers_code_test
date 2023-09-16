# 17시 01분
# 플5
# https://www.acmicpc.net/problem/17071
import heapq

n, m = map(int, input().split())

queue = []
dp = [500_001] * 500_001
queue.append([0, n])
data = set()
def calc(time):
    return time * (time+1) / 2

while queue:
    t, cur = heapq.heappop(queue)
    cm = calc(t)
    if cur == (m + cm) :
        print(t)
        exit()
    move = [cur+1, cur-1, cur*2]
    for i in move:
        if 0 <= i <= 500_000 and (t+1, i) not in data and dp[i] > t+1 :
            heapq.heappush(queue, [t+1, i])
            data.add((t+1, i))
print(-1)


# 0 <= n <= 500,000

# n, m = map(int, input().split())
#
# queue = []
# dp = [500_001] * 500_001
# queue.append([0, n])
#
# def calc(time):
#     return time * (time+1) / 2
#
# while queue:
#     t, cur = heapq.heappop(queue)
#     cm = calc(t)
#     if cur == (m + cm) or cur == (m - cm):
#         print(t)
#         exit()
#     move = [cur+1, cur-1, cur*2]
#     for i in move:
#         if 0 <= i <= 500_000 and dp[i] > t+1 :
#             heapq.heappush(queue, [t+1, i])
# print(-1)


n, m = map(int, input().split())

queue = []
dp = [500_001] * 500_001
queue.append([0, n])
data = set()
def calc(time):
    return time * (time+1) / 2

while queue:
    t, cur = heapq.heappop(queue)
    cm = calc(t)
    if cur == (m + cm) :
        print(t)
        exit()
    move = [cur+1, cur-1, cur*2]
    for i in move:
        if 0 <= i <= 500_000 and (t+1, i) not in data and dp[i] > t+1 :
            heapq.heappush(queue, [t+1, i])
            data.add((t+1, i))
print(-1)