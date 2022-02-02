def solution(genres, plays):
    answer = []
    a = { i : [] for i in genres}   #장르: 플레이횟수
    b = { i : 0 for i in genres}    #장르별 플레이 횟수 총합

    for i in range(len(genres)):
        a[genres[i]].append([i,plays[i]])   #장르: 플레이 리스트 추가
        b[genres[i]] += plays[i]            #장르: 플레이 횟수 총합

    for i, v in a.items():
        a[i] = sorted(v, key=lambda x: x[1], reverse=True)  #장르별 플레이 횟수 정렬

    b = dict(sorted(b.items(), key= lambda x: x[1] , reverse=True)) #플레이 횟수 총합 정렬
    for i, v in b.items():
        for j in range(2):
            answer.append(a[i][j][0])

    return answer