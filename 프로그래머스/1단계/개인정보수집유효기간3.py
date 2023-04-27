# 19시 55분 20시 02분
def days(y, m, d):
    return y*28*12 + m*28 + d
def solution(today, terms, pri):
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    tod = days(t_y, t_m, t_d)
    dic = {}
    for i in terms:
        alp, per = i.split(" ")
        dic[alp] = 28 * int(per)
    for v, i in enumerate(pri):
        per, alp = i.split(" ")
        y, m, d = map(int, per.split("."))
        total = days(y, m, d) + dic[alp]
        if total <= tod:
            answer.append(v+1)
    return answer