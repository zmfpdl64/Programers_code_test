#12시 39분 12시 42분

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: (x[1],x[0]))
for i in range(len(a)):
    print(' '.join(map(str, a[i])))
