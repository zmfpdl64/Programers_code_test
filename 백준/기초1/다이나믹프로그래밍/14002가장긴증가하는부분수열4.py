#2시 44분 5시
# 골4
n = int(input())
a = list(map(int, input().split()))
dp = [0] * 1001
answer = [[] for i in range(len(a))]
for i in range(len(a)):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            answer[i] = answer[j].copy()
    dp[i] += 1
    answer[i].append(a[i])
answer = sorted(answer, key = lambda x: (len(x)), reverse = True)
print(len(answer[0]))
print(*answer[0])