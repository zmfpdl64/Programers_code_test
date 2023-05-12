# 13시 13분
# 13시 20분 7분
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def trans(num, k):
    result = ''
    while num != 0:
        mod = num % k
        num = num // k
        result += str(mod)
    return result[::-1]
def isprime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    maxi = int(num**0.5) + 1
    for i in range(3, maxi):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    n = trans(n, k)
    nums = n.split("0")
    for num in nums:
        if num == '':
            pass
        else:
            if isprime(int(num)):
                answer += 1
    return answer