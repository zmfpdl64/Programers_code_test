# 15시 36분
# 15시 51분 15분
# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for tree in skill_trees:
        idx = 0
        for s in skill:
            try:
                if idx <= tree.index(s):
                    idx = tree.index(s)
                else:
                    break
            except:
                idx = 10 ** 10
        else:
            answer += 1
    return answer