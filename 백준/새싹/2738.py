import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for j in range(m):
    b.append(list(map(int, input().split())))

for i in range(len(a)):
    for j in range(len(a[i])):
        if j == len(a[i]) -1:
            print(a[i][j] + b[i][j])
        else:
            print(a[i][j] + b[i][j], end=' ')
    print()