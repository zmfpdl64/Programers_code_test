# 5시 44분 5시 47분
# 브1
n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        print(i)
        n //= i
    else:
        i+=1
