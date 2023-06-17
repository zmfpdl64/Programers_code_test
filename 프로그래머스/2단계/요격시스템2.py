# 22시 56분
# 23시 15분
# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    targets.sort(key=lambda x: x[1])
    count = 0
    sec = [0, 0]
    for i in range(len(targets)):
        target_sec = targets[i]
        if sec[1] <= target_sec[0]:
            count += 1
            sec = target_sec

    return count