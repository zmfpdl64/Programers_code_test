#12시 15분 12시 38분
import sys
n = int(sys.stdin.readline())
i = 666
answer = []
while i != 0:
    if "666" in str(i):
        answer.append(i)
        if len(answer) == n:
            break
    i += 1
answer.sort()
print(answer[-1])