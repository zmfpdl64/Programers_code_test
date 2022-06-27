#12시 03분 12시 20분

n = int(input())
i = -1
while n > 0:
    i += 1
    if i == 0:
        n -= 1
    else:
        n -= 6*i

print(i+1)