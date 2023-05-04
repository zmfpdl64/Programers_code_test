# 12시 58분

def solution(info, query):
    answer = [ ]
    lang = {"java": set(), "python": set(), "cpp": set()}
    part = {"backend": set(), "frontend": set()}
    grade = {"senior":set(), "junior":set()}
    soul = {"chicken":set(), "pizza":set()}
    score = []
    sel = [lang, part, grade, soul]
    for i, v in enumerate(info):
        info[i] = list(v.split(" "))
        score.append(info[i][-1])
        for j in range(len(sel)):
            sel[j][info[i][j]].add(i)
    for i, v in enumerate(query):
        v = " ".join(v.split(" and "))
        v = v.split(" ")
        lists = []
        result = 0
        for j in range(len(v)-1):
            if j == 0:
                if v[j] == '-':
                    list(map(lambda x: lists.extend(x), sel[j].values()))
                else:
                    lists = sel[j][v[j]]
            else:
                if v[j] == '-':
                    pass
                else:
                    lists = list(set(lists) & set(sel[j][v[j]]))
        for j in lists:
            if int(v[-1]) <= int(score[j]):
                result += 1
        answer.append(result)
    return answer
