# 16시 13분
# 16시 37분
# DP문제
def solution(land):
    maps = [land[0]]
    for i in range(1, len(land)):
        prev = land[i-1]
        line = []
        for j in range(len(land[i])):
            maxi = 0
            for k in range(len(prev)):
                if j != k:
                    maxi = max(maps[i-1][k], maxi)
            num = maxi+land[i][j]
            line.append(num)
        maps.append(line)
    return max(maps[-1])
solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])