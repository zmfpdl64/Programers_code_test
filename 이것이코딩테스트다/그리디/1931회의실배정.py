#실버1
#9시59분 10시 25분 26분걸림
# 정렬하는 기준이 매우 중요하다.
# 끝나는 시간을 기준으로 정렬하고 또한 시작하는 시간을 기준으로 정렬해야한다.
import sys
input = sys.stdin.readline
a = []
n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))
a = sorted(a, key = lambda x : (x[1]))
count = 0
curp = 0
for i in range(len(a)):
    start = a[i][0]
    end = a[i][1]
    if curp <= start:
        curp = end
        count += 1
print(count)
