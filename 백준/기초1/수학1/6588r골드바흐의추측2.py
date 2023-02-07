import sys
input = sys.stdin.readline
m = 1000001
p_map = [True] * m
p_map[1], p_map[0] = False, False
n = int(m**0.5)+1
for i in range(2, n):
    if p_map[i]:
        for j in range(i*2, m, i):
            p_map[j] = False

while True:
    num = int(input())
    result = ''
    for i in range(3, m):
        if p_map[i] and p_map[m-i]:
            if num == p_map[i] + p_map[m-i]:
                result = f'{num} = {p_map[i]} + {p_map[m-i]}'
    if result:
        print(result)
    else:
        print("Goldbach's conjecture is wrong.")