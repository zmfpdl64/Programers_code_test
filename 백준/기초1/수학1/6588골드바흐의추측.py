import sys
input = sys.stdin.readline
m = 1000001
p_map = [True] * m
p_map[1], p_map[0] = False, False
n = int(m**0.5)+1
for i in range(2, n, 2):
    if p_map[i]:
        for j in range(i*2, m, i):
            if p_map[j] == True:
                p_map[j] = False
while True:
    num = int(input())
    if num == 0:
        break
    result = ''
    for i in range(3, m, 2):
        if p_map[i] and p_map[num-i]:
            result = f'{num} = {i} + {num-i}'
            break
    if result:
        print(result)
    else:
        print("Goldbach's conjecture is wrong.")