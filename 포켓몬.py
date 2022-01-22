def solution(nums):
    b = len(nums)/2
    nums = set(nums)
    a = len(nums)
    if a >= b:
        return b
    else:
        return a

print(solution([3, 3, 3, 2, 2, 4]))

