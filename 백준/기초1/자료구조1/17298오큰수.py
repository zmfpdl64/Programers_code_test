#10시 36분
# 골4
n = int(input())
a = list(map(int, input().split()))
stack = [0]
answer = [-1] * n
for i in range(1,n):
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]
    stack.append(i)
print(*answer)