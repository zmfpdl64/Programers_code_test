a = [[False]*3 for _ in range(3)]    #행이 복사가 되서 하나의 행의 요소를 변경하면 모든 행의 수정된다.

for i in a:
    print(i)
a[1][1] = True
for i in a:
    print(i)