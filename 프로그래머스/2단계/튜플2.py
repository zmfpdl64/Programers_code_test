# 16시 30분
# 16시 41분
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    s = s[1:-1]
    s = s.replace("},", "} ").split(" ")
    dic = {}
    for i in range(len(s)):
        s[i] = list(s[i][1:-1].split(","))
    for i in s:
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
    values = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    for i in values:
        answer.append(int(i[0]))
    return answer