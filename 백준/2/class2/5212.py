# 12시 43분
import sys
input = sys.stdin.readline
r, c = map(int, input().split(" "))
maps = []
for i in range(r):
    maps.append(list(input().rstrip()))
show = [[0,1],[0,-1],[1,0],[-1,0]]
shore = []
for i in range(len(maps)):
    for j in range(len(maps[i])):
        state = maps[i][j]
        if state == "X":
            shore.append((i,j))
depre = []
for j in range(len(shore)):
    x, y= shore[j]
    count = 0
    for mx, my in show:
        nx = mx + x
        ny = my + y
        try:
            if maps[nx][ny] == '.':
                count += 1
        except:
            count +=1
    if count >= 3:
        depre.append((x, y))
for j in depre:
    x, y = j
    shore.remove(j)
    maps[x][y] = '.'
if shore:
    start_x = list(min(shore, key=lambda x: (x[0])))[0]
    start_y = list(min(shore, key=lambda x: (x[1])))[1]
    end_x = list(max(shore, key=lambda x: (x[0])))[0]
    end_y = list(max(shore, key=lambda x: (x[1])))[1]

    for i in range(start_x, end_x+1):
        print("".join(maps[i][start_y:end_y+1]))
    
    

        
            
        
            
        