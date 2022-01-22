def solution(n, arr1, arr2):
    answer = []
    
    for i, v in enumerate(arr1):
        arr1[i] = bin(arr1[i])
        arr1[i] = list(arr1[i][2:])
        while len(arr1[i]) != size:
            arr1[i].insert(0, '0')
             
    for i, v in enumerate(arr2):
        arr2[i] = bin(arr2[i])
        arr2[i] = list(arr2[i][2:])
        while len(arr2[i]) != size:
            arr2[i].insert(0, '0')
        
    d = ''  #미리 타입선언 안해주면 오류 발생
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                d += '#'
            else:
                d += ' '
        answer.append(d)
        d = ''
    return answer





arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
solution(6, arr1, arr2)
