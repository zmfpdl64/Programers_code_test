arr = [1, 2, 3, 3, 3, 3, 4, 4]
arr1 = [3, 2, 4, 4, 2, 5, 2, 5, 5]
arr2 = [3, 5, 7, 9, 1]
def solution(arr):
    arr.sort()
    dic = {}
    answer = []
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
    for i in dic.keys():
        if dic[i] > 1:
            answer.append(dic[i])
    if len(answer) == 0:
        answer.append(-1)
    print(answer)
    return answer

solution(arr)
solution(arr1)
solution(arr2)