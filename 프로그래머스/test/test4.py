def solution(lo):
    answer = []
    rate = 0
    value = 0
    for i in range(len(lo)):
        dang = lo[i][0]
        buyer = lo[i][1] + 1
        rate1 = dang / buyer
        goal = lo[i][2]
        if rate1 >= rate :
            if rate1 >= 1:
                answer.append([1,goal, i])
            else:
                answer.append([rate1,goal,i])
    answer = sorted(answer, key = lambda x : (-x[0], -x[1]))
    print(answer[0][2])
    return answer

solution([100,100,500],[1000,1000,100])