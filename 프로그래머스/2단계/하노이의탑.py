# 17시 33분
# 다시 풀기
def solution(n):
    answer = []
    def hanoi(n, start, mid, end):
        if n == 1:
            answer.append([start, end])
            return
        hanoi(n - 1, start, end, mid)
        answer.append([start, end])
        hanoi(n - 1, mid, start, end)
    hanoi(n, 1, 2, 3)

    return answer