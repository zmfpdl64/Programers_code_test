# 15시 04분 16시 18분 1시간 14분

# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import deque

def isShortestRange(range1, startIdx, endIdx):
    if range1[1] - range1[0] > endIdx - startIdx:
        return True
    return False
# def isNotContainsAll(dic):
def solution(gems):
    answer = [1, len(gems)]
    dic = {}
    start_idx = 0
    end_idx = 0
    total = 0
    cur_count = 0
    for idx, key in enumerate(gems):
        if key not in dic:
            dic[key] = deque([])
            total += 1

    while start_idx <= end_idx and end_idx <= len(gems):
        if cur_count == total:
            if isShortestRange(answer, start_idx + 1, end_idx):
                answer = [start_idx + 1, end_idx]
            jewel_list = dic[gems[start_idx]]
            jewel_list.popleft()
            if not len(jewel_list):
                cur_count -= 1
            start_idx += 1
        else:
            if end_idx == len(gems):
                pass
            else:
                jewel_list = dic[gems[end_idx]]
                if not jewel_list:
                    cur_count += 1
                jewel_list.append(end_idx)
            end_idx += 1
    return answer

# solution(
#     ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# )
#
# solution(
#     ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# )
# solution(['A','B','C','D','E'])
solution(['A', 'B', 'A', 'B', 'A', 'B', 'C'])