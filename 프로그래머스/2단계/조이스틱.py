# 미해결
from itertools import permutations as permu

alpha = {chr(i): i - 65 for i in range(65, 91)}


def minlen(pos, target):
    mini = min(pos, alpha[target])
    maxi = max(pos, alpha[target])
    print(abs(maxi - mini), mini + (25 - maxi))
    return min(abs(maxi - mini), mini + (25 - maxi))


def solution(name):
    answer = float('inf')
    for case in permu(range(len(name)), len(name)):
        print(case)
        movelen = 0
        pos = 0
        for i in range(len(case) - 1):
            mini = min(case[i], case[i + 1])
            maxi = max(case[i], case[i + 1])
            movelen += min(maxi - mini, abs(mini + len(name) - 1 - maxi))
            print(min(maxi - mini, abs(mini + len(name) - 1 - maxi)))
            movelen += minlen(pos, name[i])
            print()

            # print(movelen)
            pos = alpha[name[i]]
        movelen += minlen(pos, name[case[-1]])
        if answer >= movelen:
            print(movelen)
        answer = min(answer, movelen)
    return answer


