#12시 50분 시작
import itertools

def sosu(n):
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 1
    return 0

def solution(nums):
    test = []
    answer = 0
    result = list(itertools.combinations(nums, 3))
    for i in range(len(result)):
        if sosu(sum(result[i])):
            pass
        else:
            test.append(result[i])
            answer += 1


    print(answer)
    print(test)
    return answer

solution([1,2,3,4])
solution([1,2,7,6,4])