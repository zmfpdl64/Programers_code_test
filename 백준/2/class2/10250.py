
answer = list()
for i in range(int(input())):
    a = list(map(int, input().split()))
    if a[2] % a[0] == 0:
        ho = str(a[2] // a[0])
        dong = str(a[0])
    else:
        ho = str(a[2] // a[0] + 1)
        dong = str(a[2] % a[0])
    if len(ho) < 2:
        ho = "0" + ho
    answer.append(dong + ho)


for i in range(len(answer)):
    print(answer[i])

