#4시 4시 5분
#실3
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
stack = []
answer = []
count = 1
for num in a:
    while count <= num:
        answer.append('+')
        stack.append(count)
        count +=1
    if stack.pop() != num:
        print('NO')
        quit()
    else:
        answer.append('-')
for i in answer:
    print(i)

