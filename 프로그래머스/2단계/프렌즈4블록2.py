# 15시 26분
# 16시 12 분 46분

move = [[0, 0], [0, 1], [1, 0], [1, 1]]


def solution(m, n, board):
    answer = 0
    board = [list(i)[::-1] for i in zip(*board)]
    while True:
        remove_pos = set()
        for x in range(n - 1):
            for y in range(m - 1):
                try:
                    s = board[x][y]
                    if s != '0':
                        for mx, my in move:
                            if board[x + mx][y + my] != s:
                                break
                        else:
                            for mx, my in move:
                                remove_pos.add((x + mx, y + my))
                except:
                    pass
        if len(remove_pos) == 0:
            break
        answer += len(remove_pos)
        remove_pos = list(remove_pos)
        remove_pos.sort(key=lambda x: (-x[0], -x[1]))
        for x, y in remove_pos:
            board[x].pop(y)

    return answer