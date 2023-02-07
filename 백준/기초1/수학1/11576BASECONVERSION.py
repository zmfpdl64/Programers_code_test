#5시31분 5시 40분
# 실5

a, b = map(int, input().split())
n = int(input())
c = list(map(int, input().split()))
sum = 0
for i in range(len(c)):
    num = c.pop()
    sum += num * a**i
answer = []
while sum != 0:
    num = sum % b
    sum //= b
    answer.append(num)
print(*answer[::-1])