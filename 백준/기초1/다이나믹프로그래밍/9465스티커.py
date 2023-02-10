# 4시39분 5시30분
# 실1

n = int(input())
for i in range(n):
    m = int(input())
    da = [0] * (m+1)
    db = [0] * (m+1)
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    da[1] = a[1]
    db[1] = b[1]
    for i in range(2, len(a)):
        db[i] = max(da[i-1], da[i-2]) + b[i]
        da[i] = max(db[i-1], db[i-2]) + a[i]
    print(da, db)
    print(max(db[m],da[m]))



