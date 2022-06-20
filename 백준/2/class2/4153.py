a = list(map(int, input().split()))
answer = list()
while a[0] != 0:
    a.sort()
    if (a[0]*a[0] + a[1]*a[1] - a[2]*a[2]) == 0:
        answer.append("right")
    else:
        answer.append("wrong")
    a = list(map(int, input().split()))

for i in range(len(answer)):
    print(answer[i])
