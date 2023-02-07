#4시46분 4시 54분
# 브1
a = [i for i in '0123456789']
for i in range(26):
    a.append(chr(65+i))
n, m  = map(int, input().split())
answer = ''
while n != 0:
     num = n % m
     answer = a[num] + answer
     n = n // m
print(answer)
