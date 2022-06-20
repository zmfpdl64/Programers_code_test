import itertools

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list()    
result = list(itertools.combinations(b, 3))
max = 0
diff = a[1]
for i in range(len(result)):
    sum1 = sum(result[i])
    dif1 = a[1] - sum1
    if dif1 >= 0 and diff > dif1:
        diff = dif1

print(a[1] - diff)    
    