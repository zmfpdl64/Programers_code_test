def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        num = numbers[i]
        for j in range(len(stack) - 1, -1, -1):
            prev_idx = stack[j]
            prev_num = numbers[prev_idx]
            if prev_num < num:
                answer[prev_idx] = num
                stack.pop()
            else:
                break
        stack.append(i)

    return answer