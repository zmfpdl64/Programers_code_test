# 13시 17분 13시 40분
# 실 5
# https://www.acmicpc.net/problem/2018

n = int(input())
start = 1
end = 1
sum1 = 1
count = 0
while end <= n:
    if sum1 > n:
        sum1 -= start
        start +=1
    elif sum1 == n:
        count +=1
        sum1 -= start
        start += 1
    else:
        end += 1
        sum1 += end
print(count)