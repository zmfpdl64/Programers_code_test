# 22시 15분 22시 23분
# 브론즈 2
# https://www.acmicpc.net/problem/10093
# 시간복잡도 O(n)

n, m = map(int, input().split())
mini, maxi = min(n, m), max(n, m)
size = len(range(mini+1, maxi))
print(size)
for i in range(mini+1, maxi):
    print(i, end=" ")