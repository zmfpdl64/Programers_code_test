#20시 16분
# 미해결

from itertools import product
def solution(n, info):
    info.reverse()
    ans = [-1]
    maxd = 0
    for wl in product((True, False), repeat=11):
        t = 0
        s = sum(info[i]+1 for i in range(11) if wl[i])
        if s <= n:
            apeach = sum(i for i in range(11) if not wl[i] and info[i])
            ryan = sum(i for i in range(11) if wl[i])
            d = ryan-apeach
            if d > maxd:
                maxd = d
                ans = [info[i]+1 if wl[i] else 0 for i in range(11)]
                ans[0] += n-s
    ans.reverse()
    return ans
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(	9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))