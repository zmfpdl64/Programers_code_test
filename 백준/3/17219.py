#17시 11분 
#5초 256MB  1 <= N <= 100,000 , 1 <= M <= 100,000


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = []
answer = []
url = ""
password =""
dic = dict()
for i in range(N+M):
    a = list(input().split())
    if len(a) == 1:
        url = a[0]
        answer.append(dic[url])
    elif len(a) == 2:
        url = a[0]
        password = a[1]
        dic[url] = password
for i in answer:
    print(i)