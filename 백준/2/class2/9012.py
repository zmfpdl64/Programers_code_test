import sys
n = int(sys.stdin.readline())
de = list()
a = list()
answer = list()
for i in range(n):
    a.append(input())
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == "(":
            de.append(a[i][j])
        elif a[i][j] == ")" and len(de) != 0 and de[-1] == "(":
            de.pop()
        else:
            de.append(a[i][j])
        print(de)
        

    if len(de) == 0:
        answer.append("YES")
    else:
        answer.append("NO")
    de.clear()

for i in range(len(answer)):
    print(answer[i])
    