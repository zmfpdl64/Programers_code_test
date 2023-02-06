# 3시50분 4시
# 실2
import sys
input = sys.stdin.readline
m = 1000001
p_map = [True] * m
p_map[0],p_map[1] = False, False
sq = int(m**0.5) + 1
for i in range(2, sq, 2):
    if p_map[i]:
        for j in range(i*2, m, i):
            if p_map[j]:
                p_map[j] = False
n = int(input())
for i in range(n):
    num = int(input())
    count = 0
    for i in range(2, len(p_map)):
        if p_map[i] and p_map[num-i]:
            if i > num-i:
                break
            count+=1
    print(count)

