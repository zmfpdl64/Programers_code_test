def solution(genres, plays):
    answer = []
    #a = [{'genres': genres[i], 'id': i, 'plays': plays[i]} for i in range(len(genres)) ]
    #a = sorted(a, key=lambda x : ( x['genres'],-x['plays']))
    a = { i : [] for i in genres}   #장르: 플레이횟수
    b = { i : 0 for i in genres}    #장르별 플레이 횟수 총합

    for i in range(len(genres)):
        a[genres[i]].append([i,plays[i]])   #장르: 플레이 리스트 추가
        #a[genres[i]].extend((i, plays[i]))
        b[genres[i]] += plays[i]            #장르: 플레이 횟수 총합
    
    #a = sorted(list(a.items()), key=lambda item: (item[0], item[1]))
    for i, v in a.items():
        a[i] = sorted(v, key=lambda x: x[1], reverse=True)  #장르별 플레이 횟수 정렬
    #    a[i] = sorted()    
    #    for j in v:
    #        print(j)
    b = dict(sorted(b.items(), key= lambda x: x[1] , reverse=True))
    for i, v in b.items():
        for j in range(2):
            answer.append(a[i][j][0])
        
    #print(b)
    #print(answer)
    
    #a = sorted(a.items(), key = lambda x: )
    #a = 
    #a = dict(sorted(a.items(), key= lambda item: item[1], reverse=True))
    #a = sorted(sum(list(a.values())[:]), key= lambda x: x)
    #b = list(a.values())
    #print(sum(b[0]))
    #print(a)

    return answer


solution(["classic", "pop", "classic", "classic", "pop"], 	[500, 600, 150, 800, 2500])