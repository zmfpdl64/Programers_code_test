# 13시 1분
# 13 44분 43분
# https://school.programmers.co.kr/learn/courses/30/lessons/17679

sq = [[0,0],[0,1],[1,0],[1,1]]
def solution(m, n, board):
    answer = 0
    board = [list(i)[::-1] for i in zip(*board)]
    while True:
        remove_list= set()
        for i in range(n-1):
            for j in range(m-1):
                try:
                    now = board[i][j]
                    for x, y in sq:
                        if now != board[i+x][j+y]:
                            break
                    else:
                        for x, y in sq:
                            remove_list.add((x+i, y+j))
                except:
                    pass
        if len(remove_list) == 0:
            break
        remove_list = list(remove_list)
        remove_list.sort(key=lambda x: -x[1])
        for x, y in remove_list:
            answer +=1
            board[x].pop(y)
    return answer