#2시 51분 3시 07분
#제한 1초 512MB  1 <= N <= 10
#해결방법 다이나믹 프로그래밍으로 해결

def solution(n, goal):
    global sum
    if n > goal:
        return
    elif n == goal:
        sum += 1
    else:
        solution(n+1, goal), solution(n+2, goal), solution(n+3, goal)
    
global sum
m = int(input())
a =[]
answer = []
for i in range(m):
    n = int(input())
    sum = 0
    solution(0, n)
    a.append(sum)

for i in a:
    print(i)