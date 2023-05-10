# 11시 17분
# 11시 59분 42분

import math


def changeTime(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def solution(fees, records):
    answer = []
    base_t, base_c, add_t, add_c = fees
    end_t = 23 * 60 + 59
    check = {}
    dic = {}

    def calcFee(times):
        fee = base_c
        times -= base_t
        if times > 0:
            times = math.ceil(times / add_t)
            fee += times * add_c
        return fee

    for record in records:
        time, car, inout = record.split(" ")
        time = changeTime(time)
        if inout == 'IN':
            check[car] = time
        else:
            if car not in dic:
                dic[car] = time - check[car]
            else:
                dic[car] += time - check[car]
            del check[car]
    for key, value in check.items():
        if key not in dic:
            dic[key] = end_t - value
        else:
            dic[key] += end_t - value
    for car, time in dic.items():
        fee = calcFee(time)
        dic[car] = fee

    lists = sorted(dic.items(), key=lambda x: (x[0]))
    return filter(lambda x: x[1], lists)