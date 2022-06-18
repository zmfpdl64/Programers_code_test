#6시 32분 시작 #6시 40분 완료

a = list()
a = list(map(int, input().split()))

asc = [i for i in range(1, 9)]
dec = [i for i in range(8,0, -1)]

asc_count = 0
dec_count = 0

for i in range(8):
    if a[i] == asc[i]:
        asc_count += 1
    elif a[i] == dec[i]:
        dec_count += 1 
    else:
        break
if asc_count == 8:
    print('ascending')
elif dec_count == 8:
    print('descending')
else:
    print('mixed')