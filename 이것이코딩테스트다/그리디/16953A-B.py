# 11시 37분 11시 58분
# 실버2
a, b = map(int, input().split())
c = []
def mul2(num, count):
    if num > b:
        return
    elif num == b:
        c.append(count)
        return
    count +=1
    mul2(num*2, count)
    plus1(num*2, count)

def plus1(num, count):
    if num > b:
        return
    elif num == b:
        c.append(count)
        return
    num1 = int(str(num)+'1')
    count += 1
    mul2(num1, count)
    plus1(num1, count)
mul2(a, 1)
plus1(a, 1)
if len(c) == 0:
    print(-1)
else:
    print(min(c))