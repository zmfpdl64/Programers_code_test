#22시 38분 23시 06분  28분
def andSection(target, section):
    if target[0] < section[1]:
        return [max(target[0], section[0]), min(target[1], section[1])]
    return []
def solution(targets):
    answer = 1
    targets.sort(key=lambda x : x[0])
    section = targets[0]
    for target in targets:
        section = andSection(target, section)
        if not section:
            section = target
            answer += 1
    return answer