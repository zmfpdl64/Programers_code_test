def solution(n, computers):
    answer = 0
    link_list = []
    line_list = []
    vi_map = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                line_list.append(j)
        link_list.append(line_list)
        line_list = []
    #print(link_list)

    def check_list(vi_map, j):
        if not link_list[j]:
            return False
        #print(j)
        if vi_map[j] == False:
            vi_map[j] = True
            for i in link_list[j].copy():
                check_list(vi_map, i)
                link_list[j].pop(0)
            return True
        return False



    for i in link_list:
        for j in i:
            if check_list( vi_map, j):
                answer += 1
    #print(answer)
    return answer