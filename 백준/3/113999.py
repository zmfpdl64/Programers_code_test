#16시 56분 시작
#1초 256MB 1<= N <= 1,000, 1 <= P <= 1000
n = int(input())
a = list(map(int, input().split()))
a.sort()
sum2 = 0
for i in range(0, len(a)):
    sum2 += sum(a[:i+1])
print(sum2)