def solution(numbers):
    now = []
    answer =[]
    count = 0
    s_list = []
    met = [False] * len(numbers)
    numbers = list(numbers)
    dfs(numbers, now, answer, met)

    for i in range(len(answer)):
        answer[i] = int(''.join(answer[i])) #문자를 숫자로 변환한다. 앞자리 0을 제거하기 위함

    answer = list(set(answer))  # 같은 값을 제거하기 위함

    for i in answer:    #answer 리스트에서 소수가 존재하면 count값을 증가시킨다.
        if sosu(i):
            s_list.append(i)
            count += 1
    return count    

def sosu(n):   #소수이면 참
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def dfs(numbers, now, answer, met): #모든 경우의 수를 answer에 추가한다.
    if len(now) != 0:
        answer.append(now[:])
    if len(now) == len(numbers):
        return now
    for i in range(len(numbers)):
        if met[i] == False:
            met[i] = True
            now.append(numbers[i])
            dfs(numbers, now, answer, met)
            met[i] = False
            now.pop()



solution("17")
solution("011")
solution("0000111")
solution('013')
solution('1231')