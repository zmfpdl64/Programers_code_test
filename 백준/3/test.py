
n = 5
graph = [[] for _ in range(n+1)]
b = [[]]
for i in range(len(graph)):
    for j in range(n):
        graph[i].append(j)
print(graph)
print(len(graph))
print(len(graph[0]))
print(b)