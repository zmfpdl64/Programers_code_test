# 18시 41분
# 19시 9분 28분
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    x, y = 0, 0
    dic = {}
    move = {'L':[0,-1], 'R':[0,1], 'U':[1,0], 'D':[-1,0]}
    reverse = {'L':'R', 'R':'L', 'U':'D', 'D':'U'}
    for i in range(-5, 6):
        for j in range(-5, 6):
            dic[(i,j)] = []
    for i in list(dirs):
        try:
            mx, my = move[i]
            x += mx
            y += my
            if i not in dic[(x,y)]:
                j = reverse[i]
                dic[(x,y)] += i
                dic[(x-mx, y-my)] += j
                answer+=1
        except:
            x -= mx
            y -= my
            pass
    return answer