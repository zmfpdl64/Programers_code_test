# 18시 10분
# 18시 27분 17분
# https://school.programmers.co.kr/learn/courses/30/lessons/92342

from itertools import product
def solution(n, info):
    answer = [-1]
    info.reverse()
    maxi = 0
    for case in product([True, False], repeat=len(info)):
        arrow_c = sum([info[i]+1 for i in range(len(case)) if case[i]])
        if arrow_c <= n:
            lion = sum( [ i for i in range(len(case)) if case[i]])
            apeach = sum([ i for i in range(len(case)) if not case[i] and info[i]!=0])
            result = lion - apeach
            if result > maxi:
                maxi = result
                answer = [info[i]+1 if case[i] else 0 for i in range(len(case)) ]
                answer[0] += n-arrow_c
    return answer[::-1]

