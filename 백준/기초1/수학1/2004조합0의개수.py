#11시 18분
# 실2



n, m = map(int, input().split())
n, m = max(n, m), min(n, m)
x2 = 0
x5 = 0
for i in range(1, 60):
    num1 = 2 ** i
    num2 = 5 ** i
    x2 += n // num1
    x2 -= m // num1
    x2 -= (n-m) // num1
    x5 += n // num2
    x5 -= m // num2
    x5 -= (n-m) // num2
print(min(x2, x5))







