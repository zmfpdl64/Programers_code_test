# 20시 58분 21시 37분
from collections import deque


def solution(cacheSize, cities):
    q = deque()
    answer = 0
    if cacheSize == 0:
        return 5*len(cities)

    for i in range(len(cities)):
        # 기존 요소가 존재
        for j, v in enumerate(q):
            # 기존 요소 pop 그리고 다시 append
            if v == cities[i].lower():
                q.remove(v)
                q.append(v)
                answer += 1
                break
        # 기존 요소가 존재하지 않음
        else:
            # 요소 캐시 사이즈 초과시 교체
            if len(q) >= cacheSize:
                q.popleft()
                # 가장 밑에 인자 pop 그리고 가장 위에 append
            q.append(cities[i].lower())
            answer += 5
    return answer

solution(3, 	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(5, 		["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
