#12시 34분 12시 43분
import sys

a = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

b = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
dic = {i : 0 for i in arr}
answer = []
for i in arr:
    dic[i] += 1

for i in arr1:
    if i in dic:
        answer.append(dic[i])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))



