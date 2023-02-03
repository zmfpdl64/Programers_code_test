#12시56분 1시
#브1
n = int(input())
for _ in range(n):
    a = list(input().split())
    for i, v in enumerate(a):
        a[i] = a[i][::-1]
    print(" ".join(a))
