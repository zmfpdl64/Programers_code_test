n = int(input())
a = list()
answer = ""
for i in range(1, 1000001):
    sum = i
    a = list(str(i))
    for j in range(len(a)):
        sum += int(a[j])
    if sum == n:
        answer = ''.join(a)
        break
if len(answer) == 0:
    print(0)
else:
    print(answer)
