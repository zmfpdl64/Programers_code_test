import sys
from itertools import combinations as cb
f = open('startexample.txt','r')
input = f.readline
n = int(input()) //2
m = 2*n
stat = [list(map(int, input().split())) for _ in range(m)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2
print(allstat)
mins = 65535
for i in cb(newstat[::-1], n):
    mins = min(mins, abs(allstat - sum(i)))
print(mins)

