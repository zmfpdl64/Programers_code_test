def solution(position, height, m):
    answer = 0
    dangers = []
    for i in range(len(position)-1):
        p = position[i]
        h = height[i]
        if p+h >= position[i+1]:
            dangers.append([i+1])
        else:
            dangers.append([])

    maxi = []
    for i in range(m):
        maxi = []
        for i in range(len(dangers)):
            value = dfs(dangers, i, 0)
            if value == None:
                maxi.append(0)
            else:
                maxi.append(value)
        max_v = max(maxi)
        dangers.pop(maxi.index(max_v))
        maxi.remove(max_v)
    print(dangers)
    print(maxi)
    if len(maxi) == 0:
        return 0
    else:
        return max(maxi)

def dfs(maps, now, length):
    try:
        if len(maps[now]) != 0:
            return dfs(maps, maps[now][0], length+1)
    except:
        return length


# pos = [1,2,4,5,9,10]
# dang = [2,2,2,5,2,2]

pos = [1,2,3,4]
dang = [3,1,1,1]
print(solution(pos, dang, 0))