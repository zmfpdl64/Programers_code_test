#2시 10분 시작 해시  2시 22분 2시 52분
a = {chr(i) : i-96 for i in range(97, 123)}

n = int(input())

b = input()

answer = 0

for i in range(len(b)):
    answer += a[b[i]] * (31**i)
answer %= 1234567891 
print('{:.0f}'.format(answer))

