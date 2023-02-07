#16시 49분 시작 17시 48분 망했다....
# n : 진법
# t : 구할 숫자 수
# m : 참가 인원
# p : 본인 순서
dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def solution(n, t, m, p):
    answer = ''
    string = '0'
    p -= 1
    for i in range(1, m*t):
        string += notation(n, i) #값, n진수
    for i in range(t):
        answer += string[p]
        p+=m
    return answer.upper()


def notation(x, value):
    ret = ''
    while value > 0:

        mod = value % x
        if mod >= 10:
            mod = dic.get(mod)
            
        value = value // x
        ret += str(mod)
    return ret[::-1]

# 25 -> (8, 1)  ->(2,2) ->(0, 2) 122 -> 221 -> 9*2 + 3*2 + 1 = 18 + 6 + 1 
#
print(solution(3, 3, 2, 1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))
# print(notation(3, 3*3))
    