# 19시 32분 20시 12분 40분
# https://school.programmers.co.kr/learn/courses/30/lessons/81302

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def solution(places):
    answer = []

    def searchMap(x, y, place, vi_map, sp):
        if place[x][y] == 'P' and abs(sp[0] - x) + abs(sp[1] - y) != 0:
            return False
        for mx, my in move:
            nx, ny = x + mx, y + my
            if (0 <= nx < 5) and (0 <= ny < 5) and vi_map[nx][ny] and place[nx][ny] != 'X' and abs(nx - sp[0]) + abs(ny -sp[1]) <= 2 :
                vi_map[nx][ny] = False
                if not searchMap(nx, ny, place, vi_map, sp):
                    return False
        return True

    for place in places:
        vi_map = [[True] * 5 for _ in range(5)]
        suc = True
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    vi_map[x][y] = False
                    if not searchMap(x, y, place, vi_map, [x, y]):
                        suc = False
        if suc:
            answer.append(1)
        else:
            answer.append(0)
    return answer
