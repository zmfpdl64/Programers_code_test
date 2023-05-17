# 20시 04분
# 20시 10분

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        idx = 0
        suc = True
        for sk in skill:
            if sk in tree:
                find_idx = tree.index(sk)
                if find_idx < idx:
                    suc = False
                    break
                else:
                    idx = find_idx
            else:
                idx = float('inf')
        if suc:
            answer +=1
    return answer