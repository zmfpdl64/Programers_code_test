# 17시 25분
# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        print(sorted_candidates)
        for menu, cnt in sorted_candidates:
            if cnt > 1 and sorted_candidates[0][1] == cnt:
                answer += [menu]
        print(sorted_candidates)
        # answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])