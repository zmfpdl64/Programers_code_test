#10시38분 11시 30분
#실버1
import sys
input = sys.stdin.readline
n = int(input())
def solution():
    a = []
    m = int(input())
    count = 1
    for i in range(m):
        a.append(list(map(int, input().split())))
    a.sort()
    k = a[0][1]
    for i in range(1, len(a)):
        if k > a[i][1]:
            count += 1
            k = a[i][1]
    print(count)
for i in range(n):
    solution()