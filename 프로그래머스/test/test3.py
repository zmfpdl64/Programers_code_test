#1. 구역을 나눠야 함
#2. 구역마다 알파벳 종류와 갯수를 구해야함
#3. 구역마다 알파벳 최대 갯수를 구함
#3.1 최대 갯수가 동일하면 가장 뒤 알파벳이 점령
#4. 점령한 알파벳으로 변환
#5. 최대 알파벳의 갯수를 구함

#vi_map[] 이미 접근 했거나 분리 되어있으면 True
vi_map = []
map_section = []
move = [[1,0],[-1,0],[0,1],[0,-1]]
def solution(maps):
    answer = {}
    height = len(maps)
    width = len(maps[0])
    index = 0
    for i in range(height):
        vi_map.append([])
        for j in range(width):
            if maps[i][j] == '.':
                vi_map[i].append(True)
            else:
                vi_map[i].append(False)
    
    # print(vi_map)
    for i in range(height):
        for j in range(width):
            if vi_map[i][j] == False:
                map_section.append({})
                dfs(i, j, index, height, width, maps)
                index += 1
    for i in range(len(map_section)):
        map_section[i] = dict(sorted(map_section[i].items(), key=lambda x : (-x[1], -ord(x[0]))))
    for i in range(len(map_section)):
        key = ''
        count = 0
        for j in map_section[i]:
            if j in answer:
                answer[j] += sum(map_section[i].values())
            else:
                answer[j] = sum(map_section[i].values())
            break
    answer = dict(sorted(answer.items(), key=lambda x: -x[1]))
    answer = list(answer.items())[0]
            
    return answer


def dfs(row, col, index, max_h, max_w, maps):
    global vi_map, map_section
    if row < 0 or col < 0 or row >= max_h or col >= max_w:
        return
    else:

        if vi_map[row][col] == False:
            alpha = maps[row][col]
            if alpha in map_section[index]:     #사전 만들기 및
                map_section[index][alpha] += 1
            else:
                map_section[index][alpha] = 1

            vi_map[row][col] = True
            for y, x in move:
                move_y = row + y
                move_x = col + x
                dfs(move_y, move_x, index, max_h, max_w, maps)
    return
        

print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))