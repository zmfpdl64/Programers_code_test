#11시 29분 11시 47분 18분
#구간 합 구하기 4
#1초 256MB      1<= N, M <= 100,000   
#해결 방안 1부터 n까지 더한 수열을 각각의 배열에 저장한다.
#입력값을 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = list(map(int, input().split()))
arr = [0]
sum2 = 0
for i in a:
    sum2 += i
    arr.append(sum2)

for i in range(m):
    x, y = map(int, input().split())
    sum1 = arr[y] - arr[x-1]
    print(sum1)
