# 14시 46분
# 15시 22분 36분

def solution(want, number, discount):
    answer = 0
    dic = {want[i]: number[i] for i in range(len(want))}
    stack = []
    for i in range(len(discount)):
        ingre = discount[i]
        stack.append(ingre)
        print(i, ingre)
        if ingre in dic:
            dic[ingre] -= 1
        for key, value in dic.items():
            if value > 0:
                break
        else:
            answer = i-8
            break
        if len(stack) >= 10:
            pop = stack.pop(0)
            if pop in dic:
                dic[pop] += 1
    return answer
solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
