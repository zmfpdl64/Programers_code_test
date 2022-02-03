def solution(n, lost, reserve):
    answer = 0
    stu = [1]*n

    for i in reserve:
        stu[i-1] = 2
    for i in lost:
        stu[i-1] = 0
    
    print(stu)

    if stu[0] == 0 and stu[1] == 2:
        stu[0] = 1
        stu[1] = 1
    if stu[-1] == 0 and stu[-2] == 2:
        stu[-1] = 1
        stu[-2] = 1
    print(stu)

    for i in range(1, n-1):
        if stu[i] == 0 and stu[i-1] == 2:
            stu[i] = 1
            stu[i-1] = 1
        elif stu[i] == 0 and stu[i+1] == 2:
            stu[i] = 1
            stu[i+1] = 1
    
    for i in stu:
        if i >= 1:
            answer += 1
    print(stu)
    print(answer)       
            


    return answer


solution(5, [2, 4], [1,3,5])
solution(5, [2,4], [3])
solution(5, [1,5], [2,4])
solution(5, [1,2,3], [2,4])
solution(5, [1,2,3,5], [4])
solution(5, [],[1,2,3,4,5])
solution(12,[1,2,3,4,8,9,10,11], [9,10])