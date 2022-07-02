#20시 03분
#제한 2초 256MB   1<= n, m <= 100,000
#
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    name = input().rstrip()
    dic[name] = i
    dic[i] = name
for i in range(m):
    key = input().rstrip()
    if key.isdigit():
        print(dic[int(key)])
    else:
        print(dic[key])
