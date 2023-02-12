def solution(grid):
    global map1
    for i in range(len(grid)):
        map1.append(list(grid[i]))
    for i in range(len(map1[0])):
        if map1[0][i] == '.':
            dfs(0, i)
        if map1[len(map1)-1][i] == '.':
            dfs(len(map1)-1, i)
    for i in range(len(map1)):
        if map1[i][0] == '.':
            dfs(i, 0)
        if map1[i][len(map1)-1] == '.':
            dfs(i, 0)
    count = 0
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] != '1':
                count += 1
    print(map1)
    print(count)

def dfs(x, y):
    global map1
    try:
        if map1[x][y] != '.':
            return
        else:
            map1[x][y] = '1'
    except:
        return

    for i in move:
        a, b  = i[0],i[1]
        dfs(x+a, y+b)


move = [[1,0],[0,1],[-1,0],[0,-1]]
map1 = []
# solution([".#.","#..",".#."])
solution([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#.."
         , "...###..."])
