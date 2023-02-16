# 실3
n = int(input())

a = [list(input()) for _ in range(n)]
def solution():
    global a, maxcount
    for i in range(len(a)):
        count = 1
        for j in range(len(a)-1):
            if a[i][j] == a[i][j+1]:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 1
        count = 1
        for j in range(len(a)-1):
            if a[j+1][i] == a[j][i]:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 1
maxcount = 1
for i in range(len(a)):
    for j in range(len(a[i])-1):
        if a[i][j] != a[i][j+1]:
            a[i][j+1], a[i][j] = a[i][j], a[i][j+1]
            solution()
            a[i][j+1], a[i][j] = a[i][j], a[i][j+1]
        if a[j][i] != a[j+1][i]:
            a[j][i], a[j+1][i] = a[j+1][i], a[j][i]
            solution()
            a[j][i], a[j+1][i] = a[j+1][i], a[j][i]
print(maxcount)
