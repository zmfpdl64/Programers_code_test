import math
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    dic1 = {}
    dic2 = {}
    for i in range(len(str1)-1):
        div_str = str1[i:i+2]
        if div_str.isalpha():        
            if div_str not in dic1:
                dic1[div_str] = 1
            else:
                dic1[div_str] += 1
    for i in range(len(str2)-1):
        div_str = str2[i:i+2]
        if div_str.isalpha():
            if div_str not in dic2:
                dic2[div_str] = 1
            else:
                dic2[div_str] += 1
    total = 0
    inter = 0
    for key, value in dic1.items():
        if key in dic2:
            inter += min(value, dic2[key])
            total += max(value, dic2[key])
        else:
            total += value
    for key, value in dic2.items():
        if key not in dic1:
            total += value
    if total == 0:
        return 65536
    total = inter / total * 65536
    total = math.floor(total)
    return total
