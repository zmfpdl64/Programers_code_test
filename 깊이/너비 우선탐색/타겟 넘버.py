"""
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
"""
"""
제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
입출력 예
numbers	    target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
"""

from itertools import product

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    ops = list( product('+-', repeat = n))

    for i in ops:
        val = 0
        for op, num in zip(i, numbers):
            val += num if op == '+' else -num
        answer += (val == target)
    print(answer)
    return answer

#

        

#solution([1, 1, 1, 1, 1], 3 )
solution([4, 1, 2, 1],	4 )