def solution(x, y):
    global vi_map, n, m, a
    if a[x][y] == "X":
        return 0
    else:
        count = 0
        for i in range(n):
            if a[i][y] == ".":
                count +=1
        count1 = 0
        for j in range(m):
            if a[x][j] == ".":
                count1 += 1
        if count+count1 == n+m:
            a[x][y] = "X"
            vi_map[x][y] = 2
            for i in range(n):
                for h in vi_map:
                    print(h)
                for h in a:
                    print(h)
                if i != y:
                    vi_map[i][y] -= 1
                    print(x, y, i, vi_map[i][y])
            for j in range(m):
                if j != x:
                    vi_map[x][j] -= 1

            return 1
        elif count == n: 
            vi_map[x][y] = 1
        elif count1 == m:
            vi_map[x][y] = 1
    return 0
def solution2(x, y):
    global vi_map, n, m, a
    count = 0
    if a[x][y] == "X":
        return 0
    for i in range(n):
        if a[i][y] == ".":
            count +=1
    count1 = 0
    for j in range(m):
        if a[x][j] == ".":
            count1 += 1
    if count == n or count1 == m:
        a[x][y] = "X"
        for i in range(n):
            if i != x:
                vi_map[i][y] -= 1
        for j in range(m):
            if j != y:
                vi_map[x][j] -= 1
        return 1
    return 0
        
global n, m, vi_map, a
n, m = map(int, input().split()) # n 높이, m 넓이
vi_map = [[0] * m] * n
a = []
answer = 0
for i in vi_map:
    print(i)
for i in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(m):
        answer += solution(i, j)
for i in vi_map:
    print(i)
for i in range(n):
    for j in range(m):
        answer += solution(i, j)
print(answer)

for i in a:
    print(i)