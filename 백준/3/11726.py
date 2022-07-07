#13시 20분
#1초 256MB 1 <= n <= 1000
# https://enhjh.tistory.com/66?category=1017072
n = int(input())
a = [i for i in range(n+1)]
for i in range(3, n+1):
    a[i] = a[i-1] + a[i-2]
print(a[n] % 10007)