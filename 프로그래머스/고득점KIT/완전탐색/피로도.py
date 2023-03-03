# 9시 56분 10시 9분
# LV 2
def solution(k, dun):
    vi_map = [False] * len(dun)
    def dfs(depth, count, k):
        max_value = 0
        if depth == len(dun):
            return count
        for i in range(len(dun)):
            if vi_map[i] == False:
                vi_map[i] = True
                if dun[i][0] <= k:
                    k -= dun[i][1]
                    max_value = max(max_value, dfs(depth+1, count+1, k))
                    k += dun[i][1]
                else:
                    max_value = max(max_value, dfs(depth+1, count, k))
                vi_map[i] = False
        return max_value

    return dfs(0, 0, k)

def solution1(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer
print(solution1(80, [[80,20],[50,20],[30,10]]))