# 11시 54분
# 12시 28분 34분
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    lists = [chr(i) for i in range(65, 91)]
    m = -1
    for i in range(len(msg)):
        for j in range(len(msg) + 1, i, -1):
            str1 = msg[i:j]
            if str1 in lists and i > m:
                answer.append(lists.index(str1) + 1)
                if j != len(msg):
                    lists.append(msg[i:j + 1])
                m = j - 1
                break

    return answer