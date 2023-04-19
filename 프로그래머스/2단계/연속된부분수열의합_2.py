# 22시 42분 23시 14분  32분
def minimum(answer, ans):
    if abs(answer[1]-answer[0]) >= abs(ans[1]-ans[0]):
        return True
    return False

def solution(seq, k):
    start, end = len(seq)-1, len(seq)-1
    sum1 = seq[end]
    answer = []
    while start != -1:
        if sum1 == k:
            ans = [start, end]
            if answer:
                if minimum(answer, ans):
                    answer = ans
            else:
                answer = ans
            sum1 -= seq[end]
            end-=1
        elif sum1 < k:
            start -= 1
            sum1 += seq[start]
        else:
            sum1 -= seq[end]
            end -= 1
    return answer