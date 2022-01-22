a = 'asd23as2'
d = ''
b = []
for i in a:
    if i in '123456789':   #문자열중 정수붙혀서 리스트 만들기
        d += i
        if i == a[-1]:
            b.append(d)
    else:
        if d != '':
            b.append(d)
            d = ''
        b.append(i)
    print(b)
    
