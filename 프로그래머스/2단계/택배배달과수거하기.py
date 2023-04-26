# 20시 20분
# 20시 53분

def solution(cap, n, deli, pickups):
    deli = deli[::-1]
    pickups = pickups[::-1]
    result = 0
    p = 0
    d = 0
    for i in range(n):
        p += pickups[i]
        d += deli[i]
        while p > 0 or d > 0:
            p -= cap
            d -= cap
            result += (n-i)*2
    return result
print(solution(4, 5, [1,0,3,1,2], [0,3,0,4,0]))