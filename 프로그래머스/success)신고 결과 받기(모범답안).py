def solution(id_list, report, k):
    answer = []
    report = list(set(report))

    dic2 = {name : 0 for name in id_list}
    dic = {name : [] for name in id_list}

    for i in report:
        dic[i.split()[1]].append(i.split()[0])#신고받은사람 : 신고한사람들

    print(dic)
    

    for i in dic:
        if len(dic[i]) >= k:    #i 신고당한사람 dic[i] 신고한사람들
            for j in dic[i]:
                dic2[j] += 1
    for i in dic2:
        answer.append(dic2[i])

    print(answer)

    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
