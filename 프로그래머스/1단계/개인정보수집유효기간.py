# 20시 20시 17분
d = 1
m = 28
y = 28 * 12

def solution(today, terms, privacies):
    answer = []

    rule = {}
    t_y, t_m, t_d = map(int,today.split("."))
    today = t_y*y + t_m*m + t_d*d

    for i in terms:
        key, value = i.split(" ")
        rule[key] = int(value) * 28
    for i, v in enumerate(privacies):
        a, b = v.split(" ")
        year, month, day = map(int,a.split("."))
        sum1 = year*y + month*m + day * d + rule[b]
        if sum1 <= today:
            answer.append(i+1)
    return answer