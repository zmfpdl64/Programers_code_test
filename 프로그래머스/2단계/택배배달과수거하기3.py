# 19시 49분 19시 53분

def solution(cap, n, deli, pick):
    answer = 0
    deli = deli[::-1]
    pick = pick[::-1]
    p = 0
    d = 0
    for i in range(n):
        p += pick[i]
        d += deli[i]
        while p > 0 or d > 0:
            p -= cap
            d -= cap
            answer += (n - i) * 2

    return answer