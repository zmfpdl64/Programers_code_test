# 20시 46분 21시 20분 클리어
#256MB, 2초  2 <= n <= 100  t   1 <= height <= 100

def solution(x, y):
    global n, vi_map
    if x >= n or y >= n or 0 > x or y < 0:
        return
    if vi_map[y][x] == True:
        vi_map[y][x] = False
        solution(x+1, y), solution(x, y+1), solution(x-1, y), solution(x, y-1)
    return

t = int(input())
for _ in range(1, t+1):
    n = int(input())
    a = []
    height = [0] * 101
    vi_map = [[False]*n for _ in range(n)]  #구역 나누기 위한 맵

    for i in range(n):
        b = list(map(int, input().split()))
        for j in b:
            height[j] += 1  #안에 있는 값만 반복문 돌리기 위해 생성
        a.append(b) 
    answer = []
    for i in range(1, 101):
        if height[i] != 0:
            vi_map = [[False]*n for _ in range(n)]
            count = 0
            for y in range(n):
                for x in range(n):      #height 해수면 맵 생성
                    if i < a[y][x]:
                        vi_map[y][x] = True
            for y in range(n):          #구역 체크
                for x in range(n):
                    if vi_map[y][x] == True:
                        solution(x, y)
                        count += 1
            answer.append(count)
    print("#{} {}".format(_, max(answer)))