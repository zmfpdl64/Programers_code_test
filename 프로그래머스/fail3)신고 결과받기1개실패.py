def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    c = {}
    d = []
    for i in range(len(report)):
        report[i] = report[i].split(' ')
    for i in range(len(id_list)):
        c[id_list[i]] = 0
    for i in range(len(report)):    #이름마다 신고당한 횟수
        c[report[i][1]] += 1
    for i in range(len(id_list)):    #정지 이용자 이름
        if c[id_list[i]] >= k:
            d.append(id_list[i])
    for i in range(len(id_list)):
        c[id_list[i]] = 0
    for i in range(len(report)):
        for j in range(len(d)):
            if report[i][1] == d[j]:
                c[report[i][0]] += 1

    for i in range(len(id_list)):
        answer.append(c[id_list[i]])
        
    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
