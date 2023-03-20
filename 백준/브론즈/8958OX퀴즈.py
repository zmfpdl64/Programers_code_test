# 20시 57분 21시 02분
# 브2

def factorial(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
a = int(input())
result = list()
test = list()
for i in range(a):
    test.append(input())

for i in range(len(test)):
    count = 0
    sum = 0
    for j in range(len(test[i])):
        if test[i][j] == 'O':
            count += 1
            if count == len(test[i]) or len(test[i]) == (j+1):
                sum += factorial(count)
        else:
            sum += factorial(count)
            count = 0
    result.append(sum)
    count = 0
    sum = 0

for i in range(len(result)):
    print(result[i])