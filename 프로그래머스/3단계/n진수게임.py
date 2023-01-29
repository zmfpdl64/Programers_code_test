#15시 30분
#10진수 -> 2진수 16진수로 변환
#n = 진법, t 구할 숫자 갯수, m 참가인원, p튜브의순서
#총 자릿수 m * t 
def solution(n, t, m, p):
    answer = ''
    answer2 = ''
    p -= 1
    for i in range(m*t):
        answer2 += notation(i, n)
    for i in range(t):
        answer += answer2[p]
        p = p +m
    return answer

def notation(v, n):
    answer = ''
    while v > 0:
        v, mod = divmod(v, n)
        answer += str(mod)
    return answer[::-1]


print(solution(2,4,2,1).upper())
print(solution(16,16,2,1).upper())
print(solution(16,16,2,2).upper())