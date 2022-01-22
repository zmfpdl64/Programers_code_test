def solution(dartResult):
    answer = 0
    sum1 = []
    d = ''
    b = [] #문자 정수 분리하기
    for i in dartResult:
        if i in '1234567890':
            d += i
            if i == dartResult[-1]:
                b.append(d)
        else:
            if d != '':
                b.append(d)
                d = ''
            b.append(i)
            
    for i in range(len(b)):
        if b[i] == 'S':
            sum1.append(int(b[i-1]))
        elif b[i] == 'D':
            sum1.append(int(b[i-1])**2)
        elif b[i] == 'T':
            sum1.append(int(b[i-1])**3)
        elif b[i] == '#':
            j = len(sum1)-1
            sum1[j] = -sum1[j]
        elif b[i] == '*':
            j = len(sum1)-1
            if j == 0:
                sum1[j] *= 2
            else:
                sum1[j-1] *= 2
                sum1[j] *= 2
    answer = sum(sum1)
    
    return answer

solution('1D2S#10S')
