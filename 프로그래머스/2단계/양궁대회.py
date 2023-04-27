#20시 16분
# 미해결

import itertools
total = 0
count = 0
def solution(n, info):
    global answer
    answer = []
    a = [0] * 11
    def dfs(idx, depth):
        global total, count, answer
        if depth == n:
            peach = 0
            lion = 0
            for i in range(len(a)):
                if info[i] == 0 and a[i] == 0:
                    pass
                elif info[i] >= a[i]:
                    peach += (10-i)
                else:
                    lion += (10-i)
            if total <= lion and lion > peach:
                total = lion
                answer.append(a[::])
            return
        for i in range(idx, 11):
            a[i] += 1
            dfs(i, depth+1)
            a[i] -= 1
    dfs(0, 0)
    if total == 0:
        return [-1]
    return answer[-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(	9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))