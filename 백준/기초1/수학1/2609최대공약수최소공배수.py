#3시 38분 3시 42분
# 브1
import math


def gcd2():
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    d = a * b / c

def gcd(num1, num2):
    if num1 < num2:
        return num1
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)
def lcm(num1, num2):
    a = gcd(num1, num2)
    return num1*num2/a
a = gcd(24, 18)
b = lcm(24, 18)
print(a)
print(b)
