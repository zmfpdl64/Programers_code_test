# 10시 33분 12시
# LV 2
def solution(n, wires):
    answer = 101
    i_map = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    for x, y in wires:
        vi_map = i_map.copy()
        vi_map[x] = True
        vi_map[y] = True
        q = []
        q.extend(graph[x])
        count = 1
        while q:
            node = q.pop(0)
            if vi_map[node] == False:
                count +=1
                vi_map[node] = True
                q.extend(graph[node])
        answer = min(answer, abs(count - (n-count)))
    return answer