#11시 47분 시작 브루트 포스 공부중
def dfs(map1, a, stack, answer):
    if len(stack) == 7:
        return answer.append(stack)
    for i in range(len(a)):
        if map1[i] == False:
            map1[i] = True
            stack.append(a[i])
            dfs(map1, a, stack, answer)
            stack.pop()
            map1[i] = False
            if len(stack) == 0:
                return 

map1 = [False for i in range(9)]
a = list()
answer = list()
for i in range(9):
    a.append(int(input()))
stack = list()
dfs(map1, a, stack, answer)
print(answer)

        
