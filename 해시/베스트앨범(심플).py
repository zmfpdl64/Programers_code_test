# 우선순위 1. 장르의 총합이 큰 순서로 나열
# 우선순위 2. 장르안에서 플레이 횟수 순서로 나열
# 우선순위 3. 플레이 횟수가 동일할 경우 id로 정렬

#1. 장르의 플레이 총합을 구해서 sorted를 이용하여 정렬한다.
#2. zip()을 이용하여 리스트들을 하나의 집합으로 묶고 큰 값으로 정렬한다..
#3. b.keys()를 이용하여 장르마다 2개의 값을 #2번에서 만든 배열에서 가져와 id를 answer에 append한다.
def solution(genres, plays):
    answer = []
    c = list(zip(genres, plays, range(len(genres))))
    d = len(genres)         #리스트 갯수
    b = { i : 0 for i in genres}    #장르별 플레이 횟수 총합

    for i in range(d):
        b[genres[i]] += plays[i]            #장르: 플레이 횟수 총합
    c = sorted(c, key=lambda x: x[1], reverse= True)
    b = dict(sorted(b.items(), key= lambda x: x[1] , reverse=True)) #플레이 횟수 총합 정렬
    print(c)

    for i in b.keys():  
        count = 0
        for j in c:
            if j[0] == i:
                answer.append(j[2])
                count += 1
                if count == 2:
                    break
    
    print(answer)
            


            


    return answer

solution(["classic", "pop", "classic", "classic", "pop"], 	[500, 600, 150, 800, 2500])