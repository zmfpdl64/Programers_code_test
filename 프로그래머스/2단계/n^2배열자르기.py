# 17시 32분
# 18시 36분
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    maps = []
    l_div = left // n
    l_mod = left % n
    r_div = right // n
    r_mod = right % n
    for i in range(l_div, r_div+1):
        line = [i+1] * (i+1) + list(range(i+2, n+1))
        answer += line[:]
    return answer[l_mod: n*(r_div-l_div) + r_mod+1]