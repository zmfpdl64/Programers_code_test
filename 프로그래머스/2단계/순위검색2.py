from bisect import bisect_left
from itertools import product


def solution(info, query):
    answer = []
    table = {}
    for i in info:
        i = i.split()
        conditions = product([i[0], '-'], [i[1], '-'], [i[2], '-'], [i[3], '-'])
        for c in conditions:
            key = ''.join(c)
            if key not in table:
                table[key] = []
            table[key].append(int(i[4]))

    for key in table.keys():
        table[key].sort()

    for q in query:
        q = q.split()
        key = q[0] + q[2] + q[4] + q[6]
        if key not in table:
            answer.append(0)
        else:
            answer.append(len(table[key]) - bisect_left(table[key], int(q[7])))

    return answer