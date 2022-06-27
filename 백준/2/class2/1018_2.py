#4시 14분 시작

import sys

b_w = ""
b_b = ""
a = list(map(int, sys.stdin.readline().split()))
arr = []
for i in range(a[0]):
    arr.append(sys.stdin.readline())
for i in range(a[1]):
    if i % 2 == 0:
        b_w += "W"
    else:
        b_w += "B"
for i in range(a[1]):
    if i % 2 != 0:
        b_b += "W"
    else:
        b_b += "B"
white_ch = 0
black_ch = 0
for i in range(a[0]):
    for j in range(a[1]):
        if i % 2 == 0:
            if b_w[j] != arr[i][j]:
                white_ch += 1
        else:
            if b_b[j] != arr[i][j]:
                white_ch += 1

        if i % 2 != 0:
            if b_w[j] != arr[i][j]:
                black_ch += 1
        else:
            if b_b[j] != arr[i][j]:
                black_ch += 1
if white_ch >= black_ch:
    print(black_ch)
else:
    print(white_ch)