def solution(board, moves):
    answer = 0
    ch = []
    count = 0

    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i] != 0 and count == 0:
                ch.append(board[j][i])
                board[j][i] = 0
                if len(ch) >= 2 and (ch[-1] == ch[-2]):
                    ch.pop()
                    ch.pop()
                    answer += 2
                break
        count = 0
    return answer



c = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = 	[1,5,3,5,1,2,1,4]
solution(c, moves)
