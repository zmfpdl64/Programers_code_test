#19시   19시 08분
#1초 256MB 1 <= N <= 100,000  0 <= x <= 2^31
import heapq, sys
input = sys.stdin.readline
t = int(input())
hq, answer = [], []
for i in range(t):
    n = int(input())
    if n != 0:
        heapq.heappush(hq, (-n, n))
    else:
        if len(hq) != 0:
            answer.append(heapq.heappop(hq)[1])
        else:
            answer.append(0)

for i in answer:
    print(i)