def solution(numbers):
    def dfs(numbers, met, answer, now):
        if len(numbers) == len(now):
            answer.append(''.join(now))
            return answer
        for i in range(len(numbers)):
            if met[i] == False:
                met[i] = True
                now.append(numbers[i])
                #print(now)
                dfs(numbers,met, answer, now)
                met[i] = False
                now.pop()
        if len(now) == 0:
            return 

    answer = []
    numbers = list(map(str, numbers))
    met = [False for i in range(len(numbers))]
    now = []
    dfs(numbers, met, answer, now)
    #for i in range(len(numbers)):
    #    if met[i] == False:
    #        dfs(numbers, met, answer, now)
    answer = list(map(int, answer))
    
    print(max(answer))
    return max(answer)




solution(["6", "10", "4", "11", "1"])

