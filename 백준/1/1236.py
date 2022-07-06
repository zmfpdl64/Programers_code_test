#19시 27분 22시 09분        2시간 42분
#성지키기
#2초 128MB  1<= N, M <= 50

n, m = map(int, input().split())    #n 높이 m 넓이
a = []
for i in range(n):
    a.append(list(input()))
width = [0]*m  #넓이
height = [0]*n #높이
vi_map = [[0]*m]*n
answer = 0
for i,v in enumerate(a):
    count = 0
    for j in v:
        if j == ".":
            count += 1
    if count == m:
        height[i] = 1
    else:
        height[i] = 0
for i in range(len(a[0])):
    count = 0
    for j in range(len(a)):
        if a[j][i] == ".":
            count += 1
    if count == n:
        width[i] = 1
    else:
        width[i] = 0
for i in range(n):
    for j in range(m):
        if width[j] == 1 and height[i] == 1:
            answer += 1
            width[j], height[i] = 0, 0
answer += width.count(1)
answer += height.count(1)
print(answer)