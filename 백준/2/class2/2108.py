#1시 1분



import sys
n = int(input())
a = []
dic = {i : 0 for i in range(-4000, 4001)}
key = []
answer = 0
for i in range(n):
    b = int(sys.stdin.readline())
    dic[b] += 1
    a.append(b)
a.sort()
dic = dict(sorted(dic.items(), key=lambda x : ( -x[1], x[0])))
key = list(dic.keys())

if dic[key[0]] == dic[key[1]]:
    answer = key[1]
else:
    answer = key[0]
print(round(sum(a)/len(a)))
print(a[len(a)//2])
print(answer)
print(max(a) - min(a))














# import math
# import sys

# n = int(input())
# dic = {}
# key = []
# answer = 0
# sum = 0
# for i in range(n):
#     b = int(sys.stdin.readline())
#     sum += b
#     if b in dic:
#         dic[b] += 1
#     else:
#         dic[b] = 1
# n2 = math.floor(n/2)
# middle = 0
# dic = dict(sorted(dic.items(), key=lambda x : ( -x[1], x[0])))  #최빈값 구하기위한 key list
# key = list(dic.keys())

# if dic[key[0]] == dic[key[1]]:
#     answer = key[1]
# else:
#     answer = key[0]

# dic = dict(sorted(dic.items(), key=lambda x: (x[0], x[1])))     #중앙값, 최대 최솟값 구하기 위한 key list
# key1 = list(dic.keys())
# for i, v in dic.items():
#     n2 -= v
#     if n2 <= 0:
#         middle = i
#         break
# print(round(sum / n))   #산술평균
# print(key1[middle])   #중앙값
# print(answer)           #최빈값
# print(key1[-1] - key1[0])   # 최대 - 최소
# print(dic)