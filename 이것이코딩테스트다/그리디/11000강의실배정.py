# 7시 48분
# 골5
import sys
import heapq
input = sys.stdin.readline
n = int(input())
a = []
time = []
for i in range(n):
    a.append(list(map(int, input().split())))
a = sorted(a, key=lambda x : (x[0],x[1]))
time.append(a[0][1])
for i in range(1, len(a)):
    start = a[i][0]
    end = a[i][1]
    if start >= time[0]:
        heapq.heapreplace(time, end)
    else:
        heapq.heappush(time, end)
print(len(time))

