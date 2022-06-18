def solution(b):
    a = int(b)
    a = str(bin(a))
    a = a[2:]
    answer = 0
    print(a)
    for i in range(len(a)):
        if a[i] == '1':
            answer += 1


    print('총 사용한 막대 수: ', answer)

for i in range(1, 65):
    solution(i)

