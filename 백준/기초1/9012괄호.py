#1시1분 1시 10분
#실4
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = input().rstrip()
    stack = []
    result = ''
    for i in a:
        try:
            if i == ')':
                st = stack.pop()
                if st != '(':
                    result = 'NO'
                    break
            else:
                stack.append('(')
        except:
            result = 'NO'
            break
    if len(stack) != 0:
        result = 'NO'
    if result == 'NO':
        print(result)
    else:
        print('YES')
