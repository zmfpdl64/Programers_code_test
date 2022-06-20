a = list(map(int, input().split()))
result = list()

result.append(a[0])
result.append(a[1])
result.append(a[2] - a[0])
result.append(a[3] - a[1])

a = min(result)

print(a)