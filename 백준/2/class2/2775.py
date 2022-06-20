#6시 42분
a = [[i for i in range(1, 15)]]
answer = list()
order = list()
for i in range(int(input())):
    order.append([int(input()), int(input())])

for i in range(1, 15):  #호마다 필수 사람 테이블 구현
    b = [1]
    for j in range(1,14):
        b.append(b[j-1] + a[i-1][j])
    a.append(b)

for i in range(n):      #알고싶은 호수 선택
    y = order[i][0]
    x = order[i][1]
    answer.append(a[y][x-1])

for i in range(len(answer)):
    print(answer[i])