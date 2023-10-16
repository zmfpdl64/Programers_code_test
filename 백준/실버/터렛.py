# 16시 57분 17시 44분
# 실3
# https://www.acmicpc.net/problem/1002

import sys

input = sys.stdin.readline

n = int(input())

def caldis(x1, y1, x2, y2):
    dis = ((x1-x2) ** 2 + (y1 - y2) ** 2)
    dis **= 0.5
    return dis

for i  in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = caldis(x1, y1, x2, y2)
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dis > (r1+r2):
        print(0)
    elif dis < (r1+r2):
        l1 = r2 + dis
        l2 = r1 + dis
        if r1 == l1 or l2 == r2:
            print(1)
        elif l2 < r2 or l1 < r1:
            print(0)
        else:
            print(2)
    else:
        print(1)



