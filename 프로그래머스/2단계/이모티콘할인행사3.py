# 11시 39분 12시 55분
# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product
def solution(users, emoticons):
    answer = []
    dis = [10, 20, 30, 40]
    dis_per = {10: 0.9,20: 0.8,30: 0.7,40: 0.6}
    all_sub = 0
    all_money = 0
    for rate in product(dis, repeat=len(emoticons)):
        sub = 0
        money = 0
        for user in users:
            r_money = 0
            for i in range(len(rate)):
                if user[0] <= rate[i]:
                    r_money += emoticons[i] * dis_per[rate[i]]
            if user[1] <= r_money:
                sub += 1
            else:
                money += r_money
        answer.append([sub,money])
    answer.sort(key=lambda x : (-x[0],-x[1]))
    return answer[0]