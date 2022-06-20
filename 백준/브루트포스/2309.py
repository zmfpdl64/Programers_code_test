#11시 47분 시작 브루트 포스 공부중
import itertools as it

a = list()
answer = list()
for i in range(9):
    a.append(int(input()))
b = list(it.combinations(a, 7))
for i in range(len(b)):
    if sum(b[i]) == 100:
        answer = b[i]
        break
answer = list(answer)
answer.sort()
for i in range(len(answer)):
    print(answer[i])
        
