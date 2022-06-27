import sys

a = []
answer = []
for i in range(int(sys.stdin.readline())):
    a.append(list(map(int,sys.stdin.readline().split())))

for i in range(len(a)):
    k = 1
    for j in range(len(a)):
        if i == j:
            continue
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            k += 1
    
    answer.append(k)

print(' '.join(list(map(str, answer))))
        

    