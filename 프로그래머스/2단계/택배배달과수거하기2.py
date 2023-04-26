# 20시 9분  20시 43분
def solution(cap, n, deli, pick):
    answer = 0
    deli = deli[::-1]
    pick = pick[::-1]
    d = 0
    p = 0
    for i in range(n):
        d += deli[i]
        p += pick[i]
        while p > 0 or d > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2

    return answer