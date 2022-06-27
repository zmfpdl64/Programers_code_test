a = list(map(int, input().split()))
q = []
answer = []
for i in range(a[0]):
    q.append(input())
f_b = "BWBWBWBW"
f_w = "WBWBWBWB"
change_b = 0
change_w = 0
for i in range(a[0]-7):
    for j in range(a[1]-7):
        change_b = 0
        change_w = 0
        for n in range(8):
            for m in range(8):
                if n % 2 == 0:
                    if f_b[m] != q[i+n][j+m]:
                        change_b += 1
                else:
                    if f_w[m] != q[i+n][j+m]:
                        change_b += 1
                                        
                if n % 2 == 0:
                    if f_w[m] != q[i+n][j+m]:
                        change_w += 1
                else:
                    if f_b[m] != q[i+n][j+m]:
                        change_w += 1
        if change_w >= change_b:
            answer.append(change_b)
        else:
            answer.append(change_w)
print(min(answer))