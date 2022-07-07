#1시 42분
import itertools
a = []
answer = []
for i in range(int(input())):
    
    n = int(input())
    dic = dict()
    sum1 = 0
    for j in range(n):
        name, part = input().split()
        if part in dic:
            dic[part] += 1
        else:
            dic[part] = 1
    values = list(dic.values())
    sum1 += sum(values)
    
    result = []
    s = 1
    for i in values:
        s = s*(i+1)
    print(s-1)
    # for i in range(2, len(values)+1):
    #    result = list(itertools.combinations(values,i))
    #    for j in result:
    #     c = 1
    #     for k in j:
    #         c *= k
    #     sum1 += c
    # print(sum1)

    # for i in result:
    #     for j in i:
    #         c = 1
    #         for k in j:
    #             c *= k
    #         answer.append(c)
    #         sum1 += c