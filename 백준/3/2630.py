#17시 39분 16시 35분
#어떻게 해결해야할지 잘모르겠음
# 1초 128MB  N = 2, 4, 8, 16, 32, 64, 128
import sys
input = sys.stdin.readline
n = int(input())
p_map = []
sum_count = 0
blue_count = 0
def solution(map1):
    global blue_count
    count_b = 0
    count_w = 0
    map_length = len(map1)
    map_size = map_length ** 2
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == 1:
                count_b += 1
            else:
                count_w += 1
    if count_b == map_size:
        blue_count += 1
        return 1
    elif count_w == map_size:
        return 1
    else:
        map_1 = [map1[i][:map_length//2] for i in range(map_length//2)]
        map_2 = [map1[i][map_length//2:] for i in range(map_length//2)]
        map_3 = [map1[i][:map_length//2] for i in range(map_length//2, map_length)]
        map_4 = [map1[i][map_length//2:] for i in range(map_length//2, map_length)]
        return solution(map_1)+ solution(map_2) + solution(map_3) + solution(map_4)

    
for i in range(n):
    p_map.append(list(map(int,input().split())))

sum_count = solution(p_map)

print(sum_count-blue_count)
print(blue_count)
