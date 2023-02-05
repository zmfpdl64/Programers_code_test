# 4시 26분 35분
# 실3

n, m = map(int, input().split())
pri_map = [True] * (m+1)
sq = int(m**0.5)
answer = []
for i in range(2, m):
    if pri_map[i] == True:
        for j in range(i+i, m+1, i):
            pri_map[j] = False
for i in range(n, m+1):
    if i == 1:
        pass
    elif pri_map[i] == True:
        answer.append(i)
for i in answer:
    print(i)

