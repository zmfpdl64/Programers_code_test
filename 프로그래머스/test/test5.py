#1. 상하 좌우에 #이 없는곳에서 bfs 시작
#2. 
def solution(grid):
    global map1
    for i in grid:
        map1.append(list(i))
    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if map1[i][j] == '.':
                for x, y in move1:
                    go = 1
                    try:
                        if map1[i+x][j+y] == '#':
                            go = 0
                        else:
                            pass
                    except:
                        map1[i][j] = '1'
                        break
                    if go == 1:
                        bfs(i, j)
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] != '1':
                answer += 1
    print(answer)
    for i in map1:
        print(i)
    return answer

def bfs(x, y):
    global map1
    try:
        if map1[x][y] == '.':
            map1[x][y] = '1'
        else:
            return
    except:
        return
    for a, b in move1:
        bfs(x+a, y+b)

move = [[-1, 1], [0,1], [1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
move1 = [[1,0],[0,1],[-1,0],[0,-1]]
map1 = []
# solution([".#.", "#..", ".#."])
solution([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#.."
         , "...###..."])