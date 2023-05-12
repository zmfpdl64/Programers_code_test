# 13시 22분
# 14시    38분
# https://school.programmers.co.kr/learn/courses/30/lessons/81302'

move = [[0,1], [0,-1], [1, 0], [-1, 0]]
move = [[0,1], [0,-1], [1, 0], [-1, 0]]
def solution(places):
    answer = []
    def isGood(x, y, vi_map, place, start):
        suc = True
        for mx, my in move:
            nx = mx + x
            ny = my + y
            if 0  <= nx < len(place) and 0 <= ny < len(place[nx]) and vi_map[nx][ny] and abs(start[0] - nx) + abs(start[1] - ny) <= 2:
                vi_map[nx][ny] = False
                if place[nx][ny] == 'P':
                    return False
                elif place[nx][ny] == 'X':
                    pass
                else:
                    if not isGood(nx, ny, vi_map, place, start):
                        suc = False
        if suc:
            return True
        return False
    for place in places:
        vi_map = [[True] * len(place) for _ in range(len(place[0]))]
        suc = True
        for x in range(len(place)):
            for y in range(len(place[x])):
                if place[x][y] == 'P':
                    vi_map[x][y] = False
                    if not isGood(x, y, vi_map, place, [x,y]):
                        suc = False
        if suc:
            answer.append(1)
        else:
            answer.append(0)

    return answer