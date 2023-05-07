# 16시 48분
# 16시 3분  15분
# https://school.programmers.co.kr/learn/courses/30/lessons/60058
def div_str(w):
    dic = {"(":")", ")":"("}
    u1 = 0
    v1 = 0
    for i in range(len(w)):
        if w[i] == '(':
            u1 += 1
        else:
            v1 += 1
        if u1 == v1 != 0:
            u = w[:i+1]
            v = w[i+1:]
            if check(u):
                return u + div_str(v)
            else:
                s = '(' + div_str(v)  + ')'
                for j in u[1:-1]:
                    s += dic[j]
                return s
    return ''
def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def solution(p):
    return div_str(p)