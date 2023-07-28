# 22시 13분 22시 14분
# 브4
# https://www.acmicpc.net/problem/2752
# 시간복잡도 O(logn)

l = list(map(int, input().split()))
l.sort()
print(*l)