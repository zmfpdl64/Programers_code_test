#3시 22분 3시 42분
#골드4
import sys
from queue import PriorityQueue as q
input = sys.stdin.readline
n = int(input())
a = q()
sum = 0
for i in range(n):
    a.put(int(input()))
while(a.qsize() != 1):
    num = a.get() + a.get()
    a.put(num)
    sum += num
print(sum)
