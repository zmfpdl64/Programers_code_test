# 22시 45분
# 골1
# https://www.acmicpc.net/problem/16233
import sys
input = sys.stdin.readline
t = int(input())
ans = [-1] * t
for _ in range(t):
    n = int(input())
    size = len(str(n))
    result = 0
    if n % 9 == 0:
        for i in range(size, 0, -1):
            num = 10**i - 1
            div = n // num
            if div == 10:
                pass
                break
            n %= num
            result += div * 10**(i-1)
        else:
            ans[_] = (result*10)
    else:
        pass
print(*ans)






