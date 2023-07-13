# 22시 10분 22시 11분
# 브론즈 3
# https://www.acmicpc.net/problem/10817
# 시간복잡도 O(logn)

l = list(map(int, input().split()))
l.sort()
print(l[-2])