# 17시 31분 17시 42분

from itertools import combinations as co
from collections import Counter as counter
def solution(orders, course):
    answer = []
    for k in course:
        menu_list = []
        for o in orders:
            for i in co(o, k):
                menu_list.append(''.join(sorted(i)))
        li = counter(menu_list).most_common()
        li = sorted(li,key = lambda x : (-x[1], x[0]))
        for i in li:
            if i[1] == li[0][1] and i[1] >= 2:
                answer.append(i[0])
    return sorted(answer)