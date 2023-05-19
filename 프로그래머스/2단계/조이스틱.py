# 복습 필수
# 14시 45분 시간 미정...

def solution(name):
    idx, answer = 0, 0
    change = [min(ord(i) - ord('A'), ord('Z')-ord(i)+1) for i in name]
    movelen = float('inf')
    answer = sum(change)
    for i in range(len(name)):
        count = i+1
        while count < len(name) and name[count] == 'A':
            count += 1
        movelen = min([ movelen, 2 * i + len(name) - count, 2*(len(name)-count)+i])
    return answer + movelen