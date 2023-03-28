# 21시 06분 21시 24분


def solution(k, tangerine):
    global a
    for i in tangerine:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    a = dict(sorted(a.items(), key=lambda x : (-x[1])))
    count = 0
    for key, value in a.items():
        count += 1
        k -= value
        if k <= 0:
            return count
a = {}
