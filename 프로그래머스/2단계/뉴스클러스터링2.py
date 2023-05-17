# 14시 31분
# 15시 55분 24분

import math
def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    s1 = {}
    s2 = {}
    for i in range(len(str1)-1):
        s = str1[i:i+2]
        if s.isalpha():
            if s not in s1:
                s1[s] = 1
            else:
                s1[s] += 1
    for i in range(len(str2)-1):
        s = str2[i:i+2]
        if s.isalpha():
            if s not in s2:
                s2[s] = 1
            else:
                s2[s] += 1
    union = 0
    inter = 0
    for key, value in s1.items():
        if key in s2:
            inter += min(value, s2[key])
            union += max(value, s2[key])
        else:
            union += value
    for key, value in s2.items():
        if key not in s1:
            union+= value
    if union == 0:
            return 65536
    return math.floor(inter/union*65536)