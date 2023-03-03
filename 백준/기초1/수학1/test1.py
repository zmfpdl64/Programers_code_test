import heapq
import heapq as h
a = []
h.heappush(a, [1,2])
h.heappush(a, [1,1])
h.heappush(a, [1,3])

while a:
    print(h.heappop(a))