# 14시 48분
#
# https://school.programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = 0
    sl = len(s)
    mini = len(s)
    for i in range(2, len(s)+1):
        div = sl // i
        mod = sl % i
        if mod == 0:
            dic = {}
            length = 0
            for j in range(0, len(s)+1, i):
                s1 = s[j: j+i]
                if s1 != '':
                    if s1 not in dic:
                        dic[s1] = 1
                    else:
                        dic[s1] += 1
            for key, value in dic.items():
                print(key, value)
                if value == 1:
                    length += len(key)
                else:
                    length += len(key) +1
            print(length)
            mini = min(mini, length)
    return mini

solution("aabbaccc")