#5시23분
# 실1
m = 1000001
pr_map = [True] * m
pr_map[0] = False
sq = int(m**0.5)
for i in range(2, sq):
    if pr_map[i] == True:
        for j in range(i+i, m, i):
            pr_map[j] = False
a = []
while True:
    b = int(input())
    result = ''
    if b == 0:
        break
    for i in range(3, b//2+1):
        if pr_map[i] and pr_map[b-i]:
            result = f'{b} = {i} + {b-i}'
            break
    if result:
        print(result)
    else:
        print("Goldbach's conjecture is wrong.")