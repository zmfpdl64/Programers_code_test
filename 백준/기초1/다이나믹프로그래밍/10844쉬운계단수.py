# 4시52분
# 실1
n = int(input())
a = [[0] * 10 for i in range(101)]
a[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2, len(a)):
    a[i][0] = a[i-1][1]
    a[i][9] = a[i-1][8]
    for j in range(1, 9):
        a[i][j] = a[i-1][j-1] + a[i-1][j+1]
for i in a:
    print(i)
print(sum(a[n]))
