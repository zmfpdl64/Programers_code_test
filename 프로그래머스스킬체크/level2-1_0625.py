def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    a, b = [], []
    for i in range(len(str1)-1):
        string1 = str1[i:i+2]
        if string1.isalnum():    
            a.append(string1)
    
    for i in range(len(str2)-1):
        string2 = str2[i:i+2]
        if string2.isalnum():
            b.append(string2)

    a_copy = a.copy()

    for i in b:
        if i in a_copy:
            a_copy.remove(i)
            
    ANB = len(a) - len(a_copy)
    AUB = len(a) + len(b) - ANB
    answer = ANB / AUB
    print(answer)

    return answer

solution("FRANCE", "french")

#사용된 기술
# 1 필터링, 2 카피, 3 교집합, 4 특수문자 제거, 5 소문자 변환, 6 리스트 특정 문자 제거