#11시 03분 11시 08분

def sosu(n):
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

a = int(input())
a = list(map(int,input().split()))
answer = 0
for i in range(len(a)):
    answer += sosu(a[i])
print(answer)