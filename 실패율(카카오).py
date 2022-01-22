def solution(N, stages):
    #라운드마다 존재하는 인원
    b = {}
    answer = []
    a = list()
    for i in range(0, N+1):
        a.append(stages.count(i+1))
    for i, v in enumerate(a):
        try:
            b[i+1] = v / sum(a[i:]) * 100
        except ZeroDivisionError:
            b[i+1] = 0
    del b[N+1]  #최종통과자 삭제

    #단계별 통과 인원
    #sum(a[N:])
    #단계별 실패 인원
    #a[N]
    #실패 비율
    #a[N] / sum(a[N:])
    c = sorted(b.items(), key=lambda item: (-item[1], item[0]))
    for a in c:
        answer.append(a[0])
    
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
