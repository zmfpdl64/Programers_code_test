# 1시간 조금 넘게 걸림
# 핵심 키워드 3차원 dp
# 해당 지점에서 값은 더 커도 최종 목적지까지는 더 작을 수 있음

import heapq


direction = {
    'R':[0,1],
    'L':[0,-1],
    'T':[1,0],
    'B':[-1,0]
}
def solution(board):
    WALL = 1
    q = []
    board[0][0] = 1
    for key, value in direction.items():
        heapq.heappush(q, [0, 0, 0, key])
    while q:
        v, x, y, dir = heapq.heappop(q)
        for key, value in direction.items():
            mx = value[0]
            my = value[1]
            nx = mx + x
            ny = my + y
            value = v
            if dir == key:
                value += 100
            else:
                value += 600
            if 0 <= nx < len(board) and 0 <= ny < len(board) and (board[nx][ny] >= value or board[nx][ny] == 0) and board[nx][ny] != WALL:
                board[nx][ny] = value
                heapq.heappush(q, [value, nx, ny, key])
    answer = board[len(board)-1][len(board)-1]
    for i in board:
        print(i)
    return answer

# solution([
#     [0,0,0,0],
#     [0,0,0,1],
#     [0,0,0,1],
#     [0,1,0,0]
# ]
# )
solution([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [1,0,0,0,1],
    [1,1,1,0,0]
])
# solution([
#     [0,0,1],
#     [0,0,0],
#     [1,0,0]
# ]
# )
#
# solution(
# [[0,0,0,0,0,0,0,1],
#  [0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,1,0,0],
#  [0,0,0,0,1,0,0,0],
#  [0,0,0,1,0,0,0,1],
#  [0,0,1,0,0,0,1,0],
#  [0,1,0,0,0,1,0,0],
#  [1,0,0,0,0,0,0,0]]
# )
solution(
[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
)