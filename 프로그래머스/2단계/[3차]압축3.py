# 15시 06분
# 15시 21분 15분

def solution(msg):
    answer = []
    dic = {chr(i): i - 64 for i in range(65, 91)}
    m = 0
    for i in range(len(msg)):
        if m <= i:
            for j in range(i+1, len(msg)+1):
                s = msg[i:j]
                if s not in dic:
                    answer.append(dic[s[:-1]])
                    dic[s] = len(dic)+1
                    m = j-1
                    break
            else:
                answer.append(dic[msg[i:]])
                break
    return answer