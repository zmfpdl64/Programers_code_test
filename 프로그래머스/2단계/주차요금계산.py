# 16시 56분 18시 32분 1시간 36분
def solution(fees, records):
    answer = []
    dic, calc = {}, {}
    maxi = 23*60+59
    base_t, base_f, unit_t, unit_f = fees
    seq = []
    for i in records:
        cur_t, car_id, io = i.split(" ")
        t, m = map(int, cur_t.split(":"))
        total = t*60 + m
        if io == "IN":
            dic[car_id] = total
        else:
            in_total = dic[car_id]
            total -= in_total
            if car_id in calc:
                calc[car_id] += total
            else:
                calc[car_id] = total
            dic[car_id] = None
    for k, v in dic.items():
        if v != None:
            total = maxi - v
            if k in calc:
                calc[k] += total
            else:
                calc[k] = total
    calc = dict(sorted(calc.items(), key = lambda x: x[0]))
    for value in calc.values():
        total = value - base_t
        fee = base_f
        div = total // unit_t
        mod = total % unit_t
        if total <= 0:
            pass
        else:
            if mod > 0:
                fee += (div+1) * unit_f
            else:
                fee += div * unit_f
        answer.append(fee)
    return answer