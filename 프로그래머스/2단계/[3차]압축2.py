def solution(msg):
    answer = []
    dic = {chr(i) : i-64 for i in range(65, 91)}
    cnt = 26
    m = 0
    for i in range(len(msg)):
        for j in range(i+1,len(msg)+1):
            if m > i:
                break
            str1 = msg[i:j]
            if str1 not in dic:
                cnt+=1
                dic[str1] = cnt
                answer.append(dic[str1[:-1]])
                m = j-1
                break
            else:
                if j == len(msg):
                    answer.append(dic[str1])
                    m = j
    return answer


a = [1,2,3,4]
b = [5,6,7,8]
for x,y in zip(a, b):
    print(x, y)

