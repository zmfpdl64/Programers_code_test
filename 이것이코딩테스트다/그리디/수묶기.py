#3시 47분
# 골4
import heapq
import sys
from queue import PriorityQueue as q

input = sys.stdin.readline
n = int(input())
a = q()
mc = 0
zero = 0
sum = 0
for i in range(n):
    num = int(input())
    if num == 1:
        sum += 1
    else:
        a.put(num)
    if num < 0:
        mc += 1
    elif num == 0:
        zero = 1

if mc != 0:
    if mc % 2 == 0:
        while mc > 1:
            sum += a.get() * a.get()
            mc -= 2
        if mc == 1:
            if zero == 1:
                a.get() * a.get()
            else:
                sum += a.get()
while(a.qsize() != 0):
    if a.qsize() % 2 == 1:
        sum += a.get()
    else:
        num1 = a.get()
        num2 = a.get()
        sum +=  num1 * num2
print(sum)
# if mc % 2 == 1: #음수일 때
#     if
#
