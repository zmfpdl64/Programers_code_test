#20시 03분
#제한 2초 256MB   1<= n, m <= 100,000
# dic을 2개로 만드니 25배의 시간이 소요되었다. 메모리 소비용량도 1/3 로 줄었다.
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
