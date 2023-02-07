#4시14분 4시 25분
# 실5
import math
n = int(input())
a = map(int, input().split())

def prime(num1):
    if num1 < 2:
        return False
    for i in range(2, int(num1**0.5)+1):
        if num1 % i == 0:
            return False
    return True
count = 0
for i in a:
    if prime(i):
        count +=1
print(count)