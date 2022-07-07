# import math as ma

# def solution(n, m):
#     a = ma.factorial(n)
#     b = ma.factorial(m)
#     c = ma.factorial(m-n)
#     return int(b/(a*c))
# t = input()
# answer = []
# for i in range(int(t)):
#     n, m = list(map(int,input().split()))
#     answer.append(solution(n, m))
    
# for j in range(len(answer)):
#     print(answer[j])
   



# a = [1,2,3,4,5]
# b = [1,1,2,2,3,3,4,4,5,5]
# a_copy = a.copy()
# for i in b:
#     if i in a_copy:
#         a_copy.remove(i)

# ANB = len(a) - len(a_copy)
# AUB = len(a) + len(b) - ANB
# print(ANB/ AUB)
# a= [[1,2],[3,4],[5,6]]
# b = []
# #for i in a:
# #    b.append(max(i))
# #print(b)
# c = [1,2,3,4]
# c += 5,6,7,8
# print(c)

# a =[1,2,3,4,5]
# a += 6,7
# print(a)

# a = "1234"
# print(a.isdigit())

# a, b = "noj.am".split()
# print(a)

# import itertools as it

# a= [[1,0], [0,1]]*2
# result = list(it.permutations(a,1))

# # print(a)
# for i in result:
#     print(i)
# print(len(result))

# import sys
# s=lambda:map(int,sys.stdin.readline().split())
# n,m=s()
# a=[0]
# for i in s(): a+=[a[-1]+i]
# for i in range(m): x,y=s(); print(a[y]-a[x-1])
