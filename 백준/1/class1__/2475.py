#11시 02분 시작 11시 04분 끝

a = list(map(int, input().split()))

sum = 0
for i in range(len(a)):
    sum += (a[i]*a[i])

print(sum % 10 )