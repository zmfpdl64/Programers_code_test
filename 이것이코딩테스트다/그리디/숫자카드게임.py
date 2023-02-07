import sys

def solution(size, c_map):
    N, M = size[0], size[1]
    card_map = c_map
    result = min(c_map[0])
    for i in range(len(c_map)):
        result = max(result, min(c_map[i]))
    print(result)
solution([3, 3], [[7,3,1,8],[3,3,3,4]])