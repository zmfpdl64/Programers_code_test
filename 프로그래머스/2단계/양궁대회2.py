# 12시 15분
# 13시 31분 1시간 16분

def solution(n, info):
    lists = [0] * 11
    dic = {}

    def dfs(count, idx):
        if count == n:
            apeach = 0
            lion = 0
            for i in range(len(info)):
                if info[i] == lists[i] == 0:
                    pass
                elif info[i] < lists[i]:
                    lion += (10 - i)
                else:
                    apeach += (10 - i)
            result = lion - apeach
            if result > 0:
                if result in dic:
                    ans = max(dic[result][::-1], lists[::-1])
                    dic[result] = ans[::-1]
                else:
                    dic[result] = lists[:]
        for i in range(idx, len(info)):
            if lists[i] <= info[i]:
                lists[i] += 1
                dfs(count + 1, i)
                lists[i] -= 1
            else:
                dfs(count, i + 1)

    dfs(0, 0)
    maxi = 0
    answer = []
    for key, value in dic.items():
        if maxi < key:
            answer = value
            maxi = key
    if not answer:
        return [-1]
    else:
        return answer
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]	))