# 27.6점

def solution(a, edges):
    answer = 0
    for i in a:
        if i != 0:
            break
    else:
         return 0
    if sum(a) != 0:
        return -1
    graph = {}
    for i in edges:
        x, y = i
        if x not in graph:
            graph[x] = [y]
        else:
            graph[x].append(y)
        if y not in graph:
            graph[y] = [x]
        else:
            graph[y].append(x)
    vi_map = [True] * len(a)
    graph = dict(sorted(graph.items(), key = lambda x: (len(x[1]))))
    for key, value in graph.items():
        vi_map[key] = False
        for i in value:
            if vi_map[i] and len(graph[key]) <= len(graph[i]):
                answer += abs(a[key])
                a[i] += a[key]
                a[key] = 0

    return answer