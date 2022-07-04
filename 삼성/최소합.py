#완전 검색, 최소합
#시간 초과
import itertools as it

n = int(input())
a = []
result = []
answer = []
answer1 = []
for i in range(n):
    m = int(input())
    xy = [[1,0], [0, 1]] * (m-1)
    result = list(it.combinations(xy, m+m-2))
    for j in range(m):
        a.append(list(map(int,input().split())))

    for j in result:
        x, y = 0, 0
        sum1 = a[0][0]
        for k in range(len(j)):
            x += j[k][0]
            y += j[k][1]
            sum1 += a[x][y]
        answer.append(sum1)
    answer1.append(min(answer))
    answer.clear()
    a.clear()
for i in range(len(answer1)):
    print("#{} {}".format(i+1, answer1[i]))