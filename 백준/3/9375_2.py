#1시 42분
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
 