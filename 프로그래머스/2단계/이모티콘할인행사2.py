# 20시 02분 20시 14분
def solution(users, emoticons):
    answer = []
    result = []
    rg = [10, 20, 30, 40]
    rg2 = {10: 0.9, 20:0.8, 30:0.7, 40:0.6}
    n = len(emoticons)
    def dfs(depth):
        if depth == n:
            imo = 0
            total = 0
            for i in users:
                rate = i[0]
                maxi = i[1]
                sum1 = 0
                for j, v in enumerate(emoticons):
                    if rate <= answer[j]:
                        sum1 += rg2[answer[j]]*v
                if sum1 >= maxi:
                    imo+=1
                else:
                    total += sum1
            result.append([imo, total])
            return
        for i in rg:
            answer.append(i)
            dfs(depth+1)
            answer.pop()
    dfs(0)
    result.sort(key=lambda x: (x[0],x[1]))
    return result[-1]