#21시 03분
# 22시 00분
def solution(users, emoticons):
    answer = []
    result = []
    pro = [10, 20, 30, 40]
    dic = {10: 0.9, 20: 0.8, 30: 0.7, 40: 0.6}
    n = len(emoticons)

    def dfs(depth):
        if depth == n:
            imo = 0
            total = 0
            for i in users:
                sale = i[0]
                maxi = i[1]
                sum1 = 0
                for j, v in enumerate(answer):
                    if sale <= v:
                        sum1 += dic[v] * emoticons[j]
                if sum1 >= maxi:
                    imo += 1
                else:
                    total += sum1
            result.append([imo, total])
            return
        for i in pro:
            answer.append(i)
            dfs(depth + 1)
            answer.pop()

    dfs(0)
    result.sort(key=lambda x: (-x[0], -x[1]))
    return result[0]