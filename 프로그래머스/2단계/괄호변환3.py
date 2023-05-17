# 13시 23분
# 13시 35분 12분

dic = {"(":")", ")":"("}
def isGood(u): #3
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
def solution(p):
    if p == '': #1
        return ''
    str1 = 0
    str2 = 0
    for i in range(len(p)):
        if p[i] == '(':
            str1 +=1
        else:
            str2 +=1
        if str1 == str2 != 0:
            u, v = p[:i+1], p[i+1:] #2
            if isGood(u): #3
                return u + solution(v)
            else:
                s = '(' + solution(v) + ')' # 4-1, 4-2, 4-3
                for i in u[1:-1]: #4-4
                    s += dic[i]
                return s #4-5
