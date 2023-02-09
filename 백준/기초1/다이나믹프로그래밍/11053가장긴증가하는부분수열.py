# 실2
#ver1 완탐으로 풀기
n = int(input())
map1 = list(map(int, input().split()))
answer = []
def dfs(idx, depth):
    for i in range(idx+1, len(map1)):
        if map1[i] > map1[idx]:
            dfs(i, depth+1)
    answer.append(depth)
dfs(0, 1)
print(max(answer))