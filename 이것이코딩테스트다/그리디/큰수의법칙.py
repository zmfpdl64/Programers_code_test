import sys

f = open('./큰수의법칙input.txt', 'r')
# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# M_map = list(map(int, input().split())).sort()
N, M, K = map(int, f.readline().split())
M_map = list(map(int, f.readline().split()))
M_map.sort(reverse = True)
answer = []
values = [M_map[0], M_map[1]]
sum = 0
count = int(M / (K+1)) * K + M %(K+1)
sum += count * values[0]
sum += (M - count) * values[1]
print(sum)

