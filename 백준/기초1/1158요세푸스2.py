n, k = map(int, input().split())
a = [i for i in range(1, n+1)]
answer = []
num = 0
for i in range(n):
    num += k-1
    if num >= len(a):
        num = num % len(a)
    answer.append(a.pop(num))
print('<',", ".join(map(str, answer)), '>', sep='')
