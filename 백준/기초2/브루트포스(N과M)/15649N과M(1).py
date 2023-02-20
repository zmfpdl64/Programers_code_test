# 17시 25분 17시 33분
# 실3

# n,m=map(int, input().split())
# a=[i for i in range(1,n+1)]
# vi_map = [False] * (n+1)
# answer = []
# def dfs(depth):
#     if depth == m:
#         print(*answer)
#         return
#     for i in a:
#         if vi_map[i] == False:
#             vi_map[i] = True
#             answer.append(i)
#             dfs(depth+1)
#             answer.pop()
#             vi_map[i] = False
# dfs(0)

#-------------------------------------

import itertools as t
n,_,m=input()
for i in t.permutations(range(1,int(n)+1),int(m)):print(*i)