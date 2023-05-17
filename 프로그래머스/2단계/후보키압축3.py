# 13시 41분
# 14시 9분 28분

from itertools import combinations as combi


def solution(relation):
    rg = range(len(relation[0]))
    minicase = []

    for i in rg:  # 유일성
        for case in combi(rg, i + 1):
            rows = set()
            for row in relation:
                re = []
                for col in case:
                    re.append(row[col])
                rows.add(tuple(re))
            if len(rows) == len(relation):
                minicase.append(case)
    answer = set(minicase)
    for i in range(len(minicase)):
        for j in range(i + 1, len(minicase)):
            if set(minicase[i]).issubset(set(minicase[j])):
                answer.discard(minicase[j])

    return len(answer)