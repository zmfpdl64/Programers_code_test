# 13시 9분 13시 27분 18분

n = int(input())
for idx in range(n):
    depth = int(input())
    pascal = [[1]]
    for i in range(1, depth+1):
        line = []
        for j in range(i):
            value = 0
            if j == 0:
                value = pascal[i-1][j]
            elif j == i-1:
                value = pascal[i-1][j-1]
            else:
                value = pascal[i-1][j-1] + pascal[i-1][j]
            line.append(value)
        pascal.append(line)
    print("#{}".format(idx+1))
    for i in range(1, len(pascal)):
        print(*pascal[i])