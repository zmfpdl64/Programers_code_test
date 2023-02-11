def solution(grid):
    for i in range(len(grid)):
        grid[i] = list(grid[i])
        print(grid[i])
    for i in range(len(grid)):
        for j in range(grid[i]):
            if grid[i][j] == '.':
                for k in move:
                    x = k[0]
                    y = k[1]





solution([".#.","#..",".#."])
# solution([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#.."
#          , "...###..."])
move = [[1,0],[0,1],[-1,0],[0,-1]]