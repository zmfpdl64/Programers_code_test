# 16시 57분 17시 37분 30분걸림

T = int(input())
move = [[0,1],[1,0],[0,-1],[-1,0]]
for idx in range(1, T+1):
    n = int(input())
    maps = [[0] * n for _ in range(n)]
    maps[0][0] = 1
    count = 1
    mx, my = 0, 0
    while True:
        for nx, ny in move:
            while True:
                mx += nx
                my += ny
                if 0 <= mx < n and 0 <= my < n:
                    if maps[mx][my] == 0:
                        count += 1
                        maps[mx][my] = count
                    else:
                        mx -= nx
                        my -= ny
                        break
                else:
                    mx -= nx
                    my -= ny
                    break
        if count == n*n:
            break
    print("#{}".format(idx))
    for i in maps:
        print(*i)