def solution(n, q):
    rev_base = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    rev_base = rev_base[::-1]
    a = rev_base.split('0')
    print(a)
    for i in a:
        if is_prime_num(int(i, 10)) and int(i, 10) != 1:
            answer += 1
    print(answer)
    return answer
    

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴
solution(437674, 3)
