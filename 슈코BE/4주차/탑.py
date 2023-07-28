# 17시 10분 18시 17분
# 골5
# https://www.acmicpc.net/problem/2493


n = int(input())
ins = list(map(int, input().split()))
stack = [n-1]
ans = [0] * n
for i in range(len(ins)-1, -1, -1):
    while stack and ins[stack[-1]] <= ins[i]:
        num = stack.pop()
        ans[num] = i+1
    stack.append(i)
print(*ans)

# solution(6, [9,4, 6, 3, 7,8])



