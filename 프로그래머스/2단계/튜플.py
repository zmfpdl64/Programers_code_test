# 20시 27분 20시 59분 32분
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    dic = {}
    s = s[1:-1].replace("},", "} ")
    tuples = s.split(" ")
    for i in range(len(tuples)):
        tuples[i] = list(map(int, tuples[i][1:-1].split(",")))
    for i in tuples:
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
    dic = dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
    return list(dic.keys())