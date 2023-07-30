# 13시 45분 14시 10분
# 실 4
# https://www.acmicpc.net/problem/1940

n = int(input())
m = int(input())
ins = list(map(int, input().split()))
ins.sort()

start = 0
end = len(ins)-1
count = 0

while start < end:
    sum1 = ins[start] + ins[end]
    if sum1 > m:
        end -= 1
    elif sum1 == m:
        count +=1
        end -= 1
    else:
        start += 1
print(count)

