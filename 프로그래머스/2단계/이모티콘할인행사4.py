# 11시 01분
# 11시 14분 13분
def solution(users, emoticons):
    answer = []
    rates = [10, 20, 30, 40]

    dic = {10: 0.9, 20: 0.8, 30: 0.7, 40: 0.6}
    emo_rates = []
    n = len(emoticons)
    def dfs(depth):
        if depth == n:
            sub = 0
            total_money = 0
            for user in users:
                money = 0
                for i in range(len(emo_rates)):
                    if user[0] <= emo_rates[i]:
                        money += emoticons[i] * dic[emo_rates[i]]

                if money >= user[1]:
                    sub += 1
                else:
                    total_money += money
            answer.append([sub, total_money])
            return
        for rate in rates:
            emo_rates.append(rate)
            dfs(depth + 1)
            emo_rates.pop()

    dfs(0)
    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]
