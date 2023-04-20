#20시 23분 21시 35분

def solution(rows, columns, queries):
    answer = []
    v_map = []
    for i in range(rows):
        v_map.append([(columns)*i+(j+1) for j in range(columns)])

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        cur, nex = v_map[x1+1][y1], v_map[x1][y1]
        a = []
        for i in range(y1, y2):
            a.append(cur)
            v_map[x1][i] = cur
            cur = nex
            nex = v_map[x1][i+1]
        for i in range(x1, x2):
            a.append(cur)
            v_map[i][y2] = cur
            cur = nex
            nex = v_map[i+1][y2]
        for i in range(y2, y1, -1):
            a.append(cur)
            v_map[x2][i] = cur
            cur = nex
            nex = v_map[x2][i-1]
        for i in range(x2, x1,-1):
            a.append(cur)
            v_map[i][y1] = cur
            cur = nex
            nex = v_map[i-1][y1]

        answer.append(min(a))
    return answer