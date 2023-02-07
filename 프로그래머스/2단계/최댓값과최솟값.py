def solution(s):
    string = list(map(int,s.split()))
    answer = ''
    answer = str(min(string)) + ' ' + str(max(string))
    return answer


solution("1 2 3 4")
