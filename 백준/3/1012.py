#15시 34분  16시 28분
# 1초 512MB  T  1<= N, M <= 50  1<= K <= 2500  

#백준에서 걸어놓은 재귀함수 깊이 제한이 있는데 그것을 해제하기 위한 sys.setrecursionlimit제한을 더 깊이 걸어줘야한다.

# a = [[False] *3 for _ in range(3)]    이렇게 생성해야 한다.
# a = [[False] * 3] * 3   #행이 복사가 되서 하나의 행의 요소를 변경하면 모든 행의 수정된다.

# for i in a:
#     print(i)
# a[1][1] = True

# for i in a:
#     print(i)
import sys
sys.setrecursionlimit(10 ** 4)
def solution(x, y):
    global vi_map, n, m
    if n <= y or m <= x or x < 0 or y < 0:
        return
    if vi_map[y][x] == True:
        vi_map[y][x] = False
        solution(x, y+1), solution(x+1, y), solution(x-1, y), solution(x, y-1)
    return

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split()) # m, x은 가로길이 n, y은 세로길이

    vi_map = [[False]*m for _ in range(n)] 
    for i in range(k):
        x, y = map(int, input().split())
        vi_map[y][x] = True
    
    count = 0
    for i in range(n):
        for j in range(m):
            if vi_map[i][j] == True:    
                count += 1
                solution(j, i)
    print(count)


