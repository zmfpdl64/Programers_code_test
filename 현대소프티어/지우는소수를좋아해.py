# 11시 35분분
import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
vi_map = [True] * (n+1)
dic = {i : [] for i in range(1, n+1)}
answer = []
for i in range(m):
    a, b, c = map(int, input().split())
    dic[a].append([b,c])
    dic[b].append([a,c])
def dijkstra(start):
    dest = [1_000_000_000 for _ in range(1+n)]
    dest[start] = 0
    q = [(start, 0)]
    while q:
        cur_pos, cur_level = heapq.heappop(q)
        for nex in dic[cur_pos]:
            if nex[1] < dest[nex[0]]:
                dest[nex[0]] = nex[1]
                heapq.heappush(q, [nex[0], nex[1]])
    return dest[n]

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i != 0:
            return True
    return False
mini = dijkstra(1)
for i in range(mini+1, mini*2):
    if isprime(i):
        print(i)
        break
