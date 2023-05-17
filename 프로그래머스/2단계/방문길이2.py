# 14시 12분
# 14시 27분 15분

direct = ['U', 'D', 'R', 'L']
r_direct = ['D', 'U', 'L', 'R']
reverse = {direct[i]:r_direct[i] for i in range(4)}
move = [[1,0], [-1,0],[0,1],[0,-1]]
dic = {direct[i]: move[i] for i in range(4)}

def solution(dirs):
    answer = 0
    x, y = 0, 0
    vi_map = {(i, j) : [] for i in range(-5, 6) for j in range(-5, 6)}
    for i in dirs:
        mx, my = dic[i]
        if -5<= mx+x <= 5 and -5 <= my+y <= 5:
            x = mx+x
            y = my+y
            if i not in vi_map[(x,y)]:
                vi_map[(x,y)].append(i)
                vi_map[(x-mx,y-my)].append(reverse[i])
                answer +=1
    return answer