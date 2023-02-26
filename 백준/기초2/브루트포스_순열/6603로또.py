# 12시 31분
# 실2
import itertools as it

while(True):
    a = list(map(int, input().split()))[1:]
    if len(a) == 0:
        break
    a.sort()
    for i in it.combinations(a, 6):
        print(*i)
    print()

