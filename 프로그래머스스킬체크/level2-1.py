def solution(land):
    answer = 0
    b = list()
    a = [ max(i) for i in land]
    for i in range(len(land)):
        b.append([])
        for j in range(4):
            b[i].append([j, max(land[i])-land[i][j]])
    for i in range(len(land)):
        b[i] = sorted(b[i], key=lambda x: x[1])
        #land[i] = sorted(land[i], key= lambda x: x[1], reverse=True)
    for i in range(1,len(land)-1):
       # if b[i-1][0][0] == b[i][0][0] == b[i+1][0][0]:
        

    #print(a)
    #print(b)
    return answer

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])

"""
    a = { i : [] for i in range(4)}
    for i in land:
        for j in range(4):
            a[j].append(i[j]) 
"""