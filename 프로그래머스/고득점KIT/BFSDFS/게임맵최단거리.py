from collections import deque as d
def solution(maps):
    answer = 0
    move = [[0,1],[0,-1],[1,0],[-1,0]]
    width = len(maps[0])
    height = len(maps)
    vi_map = [[False] * width for _ in range(height)]
    def bfs():
        q = d([[0, 0, 1]])
        vi_map[0][0] = True
        while q:
            x, y, count = q.popleft()
            if x == height-1 and y == width -1:
                return count

            for nx, ny in move:
                xx = nx + x
                yy = ny + y
                if 0 <= xx < height and 0 <= yy < width and maps[xx][yy] == 1 and vi_map[xx][yy] == False:
                    vi_map[xx][yy] = True
                    q.append([xx,yy,count+1])
        return -1
    return bfs()