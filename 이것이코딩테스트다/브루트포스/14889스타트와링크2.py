import sys
from itertools import combinations as cb
f = open('startexample.txt','r')
input = f.readline
for i in range(2):
    n = int(input()) //2
    m = 2*n
    stat = [list(map(int, input().split())) for _ in range(m)]
    newstat = [sum(j[0]) + sum(j[1]) - j[0][i] for i, j in enumerate(zip(stat, zip(*stat)))]
    allstat = sum(newstat) // 2
    print(allstat)
    mins = 65535
    for i in cb(newstat[::-1], n):
        mins = min(mins, abs(allstat - sum(i)))
    print(mins)
