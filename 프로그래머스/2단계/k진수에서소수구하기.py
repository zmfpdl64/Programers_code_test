#10시 59분 11시 57분
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def ten_to_k(num, k):
    result = ""
    while num > 0:
        value = str(num % k)
        num = num // k
        result += value
    return result[::-1].split("0")
def isprime(num):
    try:
        num = int(num)
        if num == 2:
            return True
        elif num <= 1:
            return False
        for i in range(3, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    except:
        return False

def solution(n, k):
    answer = 0
    result = ten_to_k(n, k)
    for i in result:
        if isprime(i):
            answer += 1
    return answer