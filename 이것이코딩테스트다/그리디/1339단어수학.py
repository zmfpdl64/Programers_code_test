# #9시 32분 11시
# #골드4
import sys
ionput = sys.stdin.readline
n = int(input())
dic = dict()
for i in range(n):
    str1 = input()
    for i in range(len(str1)):
        c = str1[i]
        j = len(str1)-i-1
        if c in dic:
            dic[c].append(j)
        else:
            dic[c] = [j]
for key, value in dic.items():
    sum1 = 0
    for i in value:
        sum1 += 10**i
    dic[key] = sum1
dic = dict(sorted(dic.items(), key = lambda x: -x[1]))
sum2 = 0
values = list(dic.values())
for i in range(0, len(values)):
    sum2 += values[i] * (9-i)
print(sum2)

