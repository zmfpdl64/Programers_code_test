#10시 27분 10시 40분
# 브1
a = [int(input()) for _ in range(9)]
start = 0
end = len(a)-1
sum1 = sum(a)
a.sort()
while start < end:
    value = a[start] + a[end]
    if sum1 - value > 100:
        start += 1
    elif sum1 - value == 100:
        break
    else:
        end -= 1
for i in range(len(a)):
    if start != i and end != i:
        print(a[i])
