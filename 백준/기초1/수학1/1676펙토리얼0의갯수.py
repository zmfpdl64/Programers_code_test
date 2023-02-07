#10시 54분 11시18분
# 실5
n = int(input())
sum = 0
for i in range(0, n+1):
    if i != 0:
        sum *= i
    else:
        sum = 1
sum = str(sum)[::-1]
count = 0
for i in sum:
    if i == '0':
        count +=1
    else:
        break
print(count)