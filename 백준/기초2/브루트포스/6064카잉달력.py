# 18시 34분 19시
# 실1
import sys
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    max_year = lcm(m, n)
    while x <= max_year:
        if (x - y) % n == 0:
            print(x)
            break
        x += m
    else:
        print(-1)
