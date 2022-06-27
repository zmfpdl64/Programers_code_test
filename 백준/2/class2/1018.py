#4시 14분 시작

import sys

a = list(map(int, sys.stdin.readline().split()))
arr = []
answer = []
for i in range(a[0]):
    arr.append(sys.stdin.readline().rstrip())
b_w = "WBWBWBWB"
b_b = "BWBWBWBW"

white_ch = 0
black_ch = 0
for i in range(len(arr)-7):
    for j in range(len(arr[i])-7):
        white_ch = 0
        black_ch = 0
        for k in range(8):
            print()
            for l in range(8):
                if k % 2 == 0:
                    if b_w[l] != arr[i+k][j+l]:
                        # print(b_w[l], arr[i+k][j+l])

                        white_ch += 1
                else:
                    if b_b[l] != arr[i+k][j+l]:
                        print(b_b[l], arr[i+k][j+l])

                        white_ch += 1
                if k % 2 == 0:
                    if b_b[l] != arr[i+k][j+l]:
                        # print(b_b[l], arr[i+k][j+l])

                        black_ch += 1
                else:
                    if b_w[l] != arr[i+k][j+l]:
                        # print(b_w[l], arr[i+k][j+l])

                        black_ch += 1
            answer.append(black_ch)
            answer.append(white_ch)
print(answer)