#15시 40분

dic = {chr(i+64):i   for i in range(1,27)}


def solution(msg):
    answer = []
    idx = 0
    while idx < len(msg):
        for i in range(idx, len(msg)): 
            message = msg[idx:i]
            if message not in dic and message != None: #사전에 메시지가 존재하지 않을때
                dic[message] = len(dic.keys())+1
                answer.append(dic[message[:-1]])
                print(answer, dic)
                idx = i-1
                break
        else: #사전에 메시지가 존재할 때
            print(answer, dic)
            answer.append(dic[msg[idx:]])
            idx = len(msg)
        idx += 1
print(solution("KAKAO"))


        
    