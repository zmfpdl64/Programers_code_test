# 20시 39분
# 20시 50분
def solution(topping):
    answer = 0
    dic = {}
    bro = set()
    for i in range(len(topping)):
        num = topping[i]
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for i in range(len(topping)):
        num = topping[i]
        bro.add(num)
        dic[num] -= 1
        if dic[num] == 0:
            del dic[num]
        if len(bro) == len(dic):
            answer += 1
    return answer