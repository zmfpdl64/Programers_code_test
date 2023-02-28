def solution(lines):
    maps = [[False] * 101 for i in range(101)]
    point = []
    for i in lines:
        y1, x1, y2, x2 = map(int, i)
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)+1):
                if maps[x1][j] == True:
                    point.append([x1, j])
                else:
                    maps[x1][j] = True
        else:
            for j in range(min(x1, x2), max(x1, x2)+1):
                if maps[j][y1] == True:
                    point.append([j, y1])
                else:
                    maps[j][y1] = True
    length = 1
    for x, y in point:
        mini = min(left(x, y, maps, 0), right(x, y, maps, 0), up(x, y, maps, 0), down(x, y, maps, 0))+1
        if length < mini:
            print(x, y)
            length = mini
    if length == 1:
        return -1
    else:
        return length

def left(x, y, vi_map, length):
    if vi_map[x][y] == False:
        return length
    return left(x,y-1, vi_map, length+1)

def right(x, y, vi_map, length):
    if vi_map[x][y] == False:
        return length
    return right(x,y+1, vi_map, length+1)

def up(x, y, vi_map, length):
    if vi_map[x][y] == False:
        return length
    return left(x+1,y, vi_map, length+1)
def down(x, y, vi_map, length):
    if vi_map[x][y] == False:
        return length
    return down(x-1,y, vi_map, length+1)

ins = [[1,4,5,4],[2,3,4,3],[3,2,3,7],[3,6,6,6],[5,4,8,4]]
print(solution(ins))

