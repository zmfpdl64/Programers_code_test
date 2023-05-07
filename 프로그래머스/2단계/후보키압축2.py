# 17시 09분
# 17시 30분 21분

from itertools import combinations
def solution(relation):
    col_size = len(relation[0])
    nums = range(col_size)
    candidates = []
    for key_size in nums:
        for combination in combinations(nums, key_size+1):
            candidates.append(combination)
    unique = []
    for candidate in candidates:
        lists = []
        for row in relation:
            rows = []
            for col in candidate:
                rows.append(row[col])
            lists.append(tuple(rows))
        if len(set(lists)) == len(relation):
            unique.append(candidate)
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if set(unique[i]).issubset(set(unique[j])):
                answer.discard(unique[j])
    return len(answer)

a = (1, 2, 3)
b = (1, 3, 2)
c = (1,2,3)
lists = [a, b, c]
print(set(lists))