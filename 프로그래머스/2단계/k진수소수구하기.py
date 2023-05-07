# 14시 19분
# 14시 29분 10분
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def prime(k):
    if k == '':
        return False
    k = int(k)
    if k <= 1:
        return False
    if k == 2:
        return True
    n = int(k ** 0.5)+1
    for i in range(3, n):
        if k % i == 0:
            return False
    return True
def transnum(n, k):
    ans = ''
    while n != 0:
        ans += str(n % k)
        n = n // k
    return ans[::-1]
def solution(n, k):
    answer = 0
    # 1. n진수 변환
    n = transnum(n, k)
    # 2. 0을기준으로 숫자 분리
    lists = n.split("0")
    for i in lists:
        if prime(i):
            answer +=1
    # 3. 소수 확인
    return answer