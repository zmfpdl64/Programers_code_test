# 13시 27분 13시 39분
T = int(input())
for idx in range(1, T+1):
    n, m =map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    maxi = 0
    for x in range(n-m):
        for y in range(n-m):
            value = 0
            for x_v in range(m):
                for y_v in range(m):
                    value += maps[x+x_v][y+y_v]
            maxi = max(maxi, value)
    print("#{} {}".format(idx, maxi))
