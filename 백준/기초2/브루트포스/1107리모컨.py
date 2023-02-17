# 19시 55분 20시 35분
# 골5
goal = int(input())
n = int(input())
a = [1] * 10
if n != 0:
    ins = list(map(int, input().split()))
    for i in ins:
        a[i] = 0
start = 100
maxi = 1_000_000
mini = abs(goal-100)
for i in range(0, maxi):
    nums = list(str(i))
    for j, v in enumerate(nums):
        if a[int(v)] == 0:
            break
        else:
            if j == len(nums)-1:
                mini = min(mini, abs(goal-i)+len(nums))
print(mini)