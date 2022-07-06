#22시 10분
#1초 128MB   1<= t <= 100   0<= n <= 30
# hat, headgear, sungglasses, turban
#조합론 내가 굉장히 약한거 같다. .....
import itertools

answer = []
for i in range(int(input())):
    m = int(input())
    dic = dict()
    for j in range(m):
        name, part = input().split()
        if part in dic:
            dic[part].append(name)
        else:
            dic[part] = [name]
    values = list(map(lambda x: int(len(x)), dic.values()))
    # print(values)
    result = []
    result.append(values)
    for i in range(2, len(values)+1):
        result.append(list(itertools.permutations(values, i)))
    # print(result)
    sum0 = 0
    for i in range(len(result)):
        sum1 = 0
        for j in range(len(result[i])):
            sum2 =0
            for k in range(len(result[i][j])):
                sum2 += result[i][j][k]
            
            sum1 += sum2
        sum0 += sum1
                
    print(sum0)
# 1
# 6
# hat head
# sung eye
# swet body
# jean under
# sandle shoes
# t-shirt body