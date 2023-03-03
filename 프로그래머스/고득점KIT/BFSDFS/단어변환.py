from collections import deque as d
def solution(begin, target, words):
    words.append(begin)
    vi_map = {i : False for i in words}
    graph = { i : [] for i in words}
    graph[begin] = []
    for i in range(len(words)):
        for j in range(len(words)):
            count = 0
            for k in range(len(words[i])):
                if words[i][k] == words[j][k]:
                    count +=1
            if count == len(words[i])-1:
                graph[words[i]].append(words[j])
    print(graph)
    q = d([[begin, 0]])
    while q:
        word, count = q.popleft()
        if word == target:
            return count
        for value in graph[word]:
            if vi_map[word] == False:
                vi_map[word] = True
                for i in graph[word]:
                    if not vi_map[i]:
                        q.append([i, count+1])
    return 0