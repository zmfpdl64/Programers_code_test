#13시 01분 오름차순 2   13시 15분
import sys

a = []

for i in range(int(sys.stdin.readline())):
    a.append(int(sys.stdin.readline()))

a.sort()

for i in range(len(a)):
    print(a[i])
