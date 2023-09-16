# 2시 43분 4시 20분
# 골4
# https://www.acmicpc.net/problem/1430

# 탑 갯수 1 <= n <= 50
# 좌표 0 <= x, y <= 1000
# 에너지 d  1 <= d <= 100
# 사정거리 r 1 <= r <= 500
# 재분배 가능
# r보다 작다면 제한내의 에너지 공유 가능
# 에너지 공유 시 절반만 전달
# 적과 거리는 r보다 작아야함
# 공격시 모든 에너지를 쏨

"""
4 2 10 0 0 탑 갯수(n), 사정거리(r), 에너지(d), x, y
2 0
4 0
6 0
8 0
"""
import heapq
import sys
import math

input = sys.stdin.readline
n, r, d, x, y = map(int, input().split())
tower = [[x, y]]
graph = { i : [] for i in range(n+1)}
vi_map = [False] * (n+1)
total = 0

# 타워 입력받기
for i in range(n):
    tower.append(list(map(int, input().split())))
# 1/2 * n (n - 1)
# 일정 거리 안에 있는 타워들을 연결한다
for i in range(len(tower)):
    for j in range(i+1, len(tower)):
        x1, y1 = tower[i]
        x2, y2 = tower[j]
        dis = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
        if dis <= r:
            graph[i].append([dis,j])
            graph[j].append([dis,i])

def bfs():
    global total
    queue = [[0, 0, 0]]
    vi_map[0] = True
    # 1/2* n (n-1)
    while queue:
        # t(적으로 부터 움직인 횟수)
        # dis (적과의 거리)
        # id (tower 식별값)
        t, dis, id = heapq.heappop(queue)

        for _dis, _nex in graph[id]:
            if not vi_map[_nex]:
                vi_map[_nex] = True
                total += d * (2 ** -t)
                heapq.heappush(queue, [t+1, _dis, _nex])
bfs()

if isinstance(total, int):
    print(f'{total:.1f}')
else:
    print(total)



