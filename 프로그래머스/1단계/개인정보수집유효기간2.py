# 20시 53분
# 21시 01분


def solution(today, terms, privacies):
    answer = []

    t_y, t_m, t_d = map(int, today.split("."))
    today = t_y * 28 * 12 + t_m * 28 + t_d
    dic = {}
    for i, v in enumerate(terms):
        alpha, peri = v.split(" ")
        dic[alpha] = int(peri) * 28
    for i, v in enumerate(privacies):
        st, al = v.split(" ")
        y, m, d = map(int, st.split("."))
        total = y * 28 * 12 + m * 28 + d + dic[al]
        if total <= today:
            answer.append(i + 1)
    return answer