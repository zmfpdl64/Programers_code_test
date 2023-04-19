# 20시 58분 22시
import re
import itertools
import copy as c


def solution(pre):
    # 1. 연산자의 모든 경우의 순서를 만든다.
    # 2. 모든 경우의 수 를 연산시켜 최댓값을 만들어낸다.
    index = ['-', '+', '*']
    li = re.split("[-+*]", pre)
    ex = re.findall("[\-\+\*]", pre)
    exp = itertools.permutations(index, 3)
    maxi = 0
    for i in exp:
        e = c.deepcopy(ex)
        l = c.deepcopy(li)
        for j in i:
            while True:
                if j in e:
                    idx = e.index(j)
                    l.insert(idx, str(eval(l.pop(idx)+e.pop(idx)+l.pop(idx))))
                else:
                    break
        l = list(map(int, l))
        maxi = max(maxi, abs(sum(l)))

    return maxi

solution("100-200*300-500+20"	)
solution("50*6-3*2")