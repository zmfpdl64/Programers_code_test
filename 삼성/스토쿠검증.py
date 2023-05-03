# 18시 37분 19시 08분 31분
T = int(input())
def row(maps):
    stack = [i for i in range(1, 10)]
    for x in range(len(maps)):
        line = stack[:]
        for y in range(len(maps)):
            value = maps[x][y]
            line.remove(value)
        if y == 8 and line:
            return 0
    return 1

def col(maps):
    stack = [i for i in range(1, 10)]
    for y in range(len(maps)):
        line = stack[:]
        for x in range(len(maps)):
            value = maps[x][y]
            line.remove(value)
        if len(line)!=0 and x == 8:
            return 0
    return 1

def block(maps):
    stack = [i for i in range(1, 10)]
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            line = stack[:]
            for nx in range(x, x+3):
                for ny in range(y, y+3):
                    line.remove(maps[nx][ny])
            if nx == 2 and line:
                return 0
    return 1
for idx in range(1, T+1):
    maps = [list(map(int, input().split())) for _ in range(9)]
    for i in maps:
        print(i)
    result = 0
    try:
        if row(maps) == col(maps) == block(maps) == 1:
            result = 1
        print("#{} {}".format(idx, result))
    except:
        print("#{} {}".format(idx, result))


