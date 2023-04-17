# 23시 08분 23시 48분
def solution(sequence, k):
    answer = []
    left, right = 0, 0
    current_sum = sequence[0]
    shortest_length = float('inf')

    while right < len(sequence):
        if current_sum < k:
            right += 1
            if right == len(sequence):
                break
            current_sum += sequence[right]
        else:
            if current_sum == k and right - left + 1 < shortest_length:
                answer = [left, right]
                shortest_length = right - left + 1
            current_sum -= sequence[left]
            left += 1

    return answer