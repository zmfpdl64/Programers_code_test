n = int(input())
def solution(num):
    result = ""
    for i in range(len(num)-2, -1, -1):
        b = []
        for j in range(i+1, len(num)):
            if int(num[i]) < int(num[j]):
                b.append([i, j, int(num[j]) - int(num[i])])
        b = sorted(b, key = (lambda x: x[2])) # 정렬
        if len(b) != 0:
            i = b[0][0]
            j = b[0][1]
            str1 = list(num)
            str1[i], str1[j] = str1[j], str1[i] # 연속대입
            l = list(str1[i+1:]) #슬라이싱
            l.sort()
            result = "".join(str1[:i+1]) + "".join(l) #리스트 -> 문자열
            break
    if not result:
        print(result)
    else:
        print('BIGGEST')
for _ in range(n):
    solution(input())
