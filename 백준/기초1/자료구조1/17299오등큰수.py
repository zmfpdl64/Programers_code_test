# 8시 37분 9시 20분
# 골3

n = int(input())
a = list(map(int, input().split()))
c_map = [0] * 1000001
stack = [0]
answer = [-1] * n
for i in a:
    c_map[i] +=1

for i in range(1, len(a)):
    while stack and c_map[a[stack[-1]]] < c_map[a[i]]:
        answer[stack.pop()] = a[i]
    stack.append(i)
print(*answer)
