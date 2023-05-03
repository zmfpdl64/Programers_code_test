# 13시 45분 14시 09분 24분
T = int(input())
for _ in range(1, T+1):
    idx = int(input())
    nums = list(map(int, input().split()))
    dic = {}
    maxi = 0
    for i, v in enumerate(nums):
        if not v in dic:
            dic[v] = 1
        else:
            dic[v] += 1
    maxi = max(dic.items(), key= lambda x: (x[1],x[0]))
    print("#{} {}".format(idx, maxi[0]))