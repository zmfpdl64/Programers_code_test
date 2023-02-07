# # #4시 29분 7시 47분 저녁 먹고 품
# # #골4
#
import heapq
import sys

input = sys.stdin.readline
n = int(input())
a = []
ma = []
sum = 0
zero = 0
for i in range(n):
    num = int(input())
    if num > 0:
        if num == 1:
            sum += 1
        else:
            a.append(num)
    else:
        if zero == 0 and num == 0:
            ma.append(0)
            zero = 1
        else:
            if num != 0:
                ma.append(num)
a.sort()
ma.sort()
while len(ma) != 0:
    if len(ma) == 1:
        sum += ma.pop(0)
    else:
        sum += ma.pop(0) * ma.pop(0)
while len(a) != 0:
    if len(a) == 1:
        sum += a.pop()
    else:
        sum += a.pop() * a.pop()
print(sum)
