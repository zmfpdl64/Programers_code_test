# 17시 25분 19시 2분
# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations as co
def counter(maps):
    dic = {}
    for i in range(len(maps)):
        for j in range(i, len(maps)):
            if maps[i] == maps[j]:
                if maps[i] not in dic:
                    dic[maps[i]] = 1
                else:
                    dic[maps[i]] += 1
    return sorted(dic.items(), key=lambda x: (-x[1], x[0]))
def popular_menu(dic, k):
    menus = []
    for key, value in dic:
        if value >= 2 and dic[0][1] == value:
            menus.append(key)
    return menus
def solution(orders, course):
    answer = []
    for i in course:
        menu_list = []
        for k in orders:
            for j in co(k, i):
                j = ''.join(sorted(j))
                menu_list.append(j)
        dic = counter(menu_list)
        answer += popular_menu(dic, i)
    return sorted(answer)