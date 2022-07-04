#18시 18분
# 0.25초 128MB  0 <= N < 40
#해결 방법 메모리 제이션을 이용한 시간 단축
#global 변수를 사용하여 함수에서 조작 가능
import sys

def fibonacci(n):
    global one, zero
    global dic
    if n in dic:
        zero += dic[n][0]
        one += dic[n][1]
    elif n == 1:
        dic[n] = [0, 1]
        one = 1
        return
    elif n == 0:
        dic[n] = [1, 0]
        zero = 1
        return
    else:
        fibonacci(n-1), fibonacci(n-2)
        dic[n] = [dic[n-1][0]+dic[n-2][0], dic[n-1][1] + dic[n-2][1]]
one = 0
zero = 0
dic = dict()
input = sys.stdin.readline
n = int(input())
a = []

for i in range(n):
    one, zero = 0, 0
    m = int(input().rstrip())
    fibonacci(m)
    a.append("{} {}".format(zero, one))

for i in a:
    print(i)