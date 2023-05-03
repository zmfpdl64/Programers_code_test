# 19시 32분 20시 03분 30분

T = int(input())
def line(in_map, lenth):
    result = 0
    for i in range(len(in_map)):
        count = 0
        list = []
        for j in range(len(in_map)):
            if in_map[i][j] == 1:
                count += 1
            else:
                list.append(count)
                count = 0
        list.append(count)
        result += list.count(lenth)
    return result
for idx in range(1, T+1):
    n, k = map(int, input().split())
    result = 0
    maps = [list(map(int, input().split())) for _ in range(n)]
    result += line(maps, k)
    map2 = list(map(list,zip(*maps)))
    result += line(map2, k)
    print("#{} {}".format(idx, result))

