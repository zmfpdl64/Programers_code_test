a = int(input())

for i in range(a-1, -1, -1):
    st = ' '*a
    st = st[:i]
    st = st + "*"*(a-(i))
    print(st)
    