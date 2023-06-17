# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def check(w):
    if w == '':
        return True
    stack =[]
    for i in w:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def div_str(p):
    dic = {")":"(", "(":")"}
    if p == '':
        return ''
    str1 = 0
    str2 = 0
    for c in range(len(p)):
        i = p[c]
        if i == '(':
            str1 += 1
        else:
            str2 += 1
        if str1 == str2 and str1 >=1:
            if check(p[:c+1]):
                return p[:c+1] + div_str(p[c+1:])
            else:
                s = '(' + div_str(p[c+1:]) +')'
                for j in range(1, len(p[:c+1])-1):
                    s += dic[p[:c+1][j]]
                return s
    return ''