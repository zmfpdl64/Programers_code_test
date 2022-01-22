#조건
#1. 투자했을 때의 이득 리스트 작성
#2. 이득리스트를 기준으로 최댓값을 만드는 리스트 생성
#3. 이득리스트에서 같은 점수일 때 더 많은 요소가 있는  리스트 선택
#4. 이득값 비교를 통한 승리 가능성
import time
import numpy as np

def solution(n, info):
    answer = [0] * len(info)
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    b = []          #최댓값 리스트
    count = 0       #하위배열 선택하기 위한 반복수 계산
    sum = 0         #상위 값과 하위값 비교하기 위한 변수
    idx = []        #변경할 list index 값 저장
    score1 = 0
    score2 = 0
    for i in range(len(a)): #1. 투자했을 때의 이득 점수 환산
        if info[i] != 0:
            b.append(round((a[i]*2/(info[i]+1)), 3))
        else:
            b.append(a[i])    
    dic = { ind : val for ind, val in enumerate(b)} 
    dic = dict(sorted(dic.items(), key=lambda item: (-item[1], item[0])))

    for i in dic:           #2. 최댓값 선택
        if n >= info[i]+1 and n != 0:
            answer[i] += info[i]+1
            n -= info[i]+1
            score1 += dic[i]
        if i == len(dic)-1 and n > 0:
            answer[i] = n
            n = 0
    for i in answer:            #3. 하위 배열에서 같은 값일 때 더 많이 선택
        if i >= 2:
            for j in range(i+1, len(answer)):
                if answer[j] == 0 and info[j] < i-1:
                    sum += b[j]
                    idx.append(j)
                    count += info[j]+1
                    if sum/count >= b[i]:                   
                        if count == i:
                            for k in idx:
                                answer[k] = 1
                            answer[i] = 0
                            break
            sum = 0
            count = 0
            idx = []
             
    for i in range(len(answer)):  #score2의 최댓값
        if answer[i] == 0 and info[i] != 0:
            score2 += len(answer) - i

    if score1 <= score2:        #우승 가능성
        return [-1]
    print(b)    #이득값 계산
    print(info) #info 배열
    print(answer)   #이득리스트 
    return answer


while True:
    a = np.random.randint(low=0, high=4, size=11)
    solution(10, a)
    time.sleep(1)    
#solution(5, [2,1,1,1,0,0,0,0,0,0,0])
#solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])
#solution(9, [0,0,1,2,0,1,1,1,1,1,1])

