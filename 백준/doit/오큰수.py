# 18시 53분 19시 4분
# 곩4
# https://www.acmicpc.net/problem/17298

n = int(input())
a = list(map(int ,input().split()))
result = [-1] * n
pop_list = []
for i in range(len(a)):
    while pop_list and a[pop_list[-1]] < a[i]:
        result[pop_list.pop()] = a[i]
    pop_list.append(i)
print(*result)