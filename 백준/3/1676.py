#17시 56분

from math import factorial as fa

n = int(input())

n = str(fa(n))
n = n[::-1]
count = 0
for i in n:
    if i == "0":
        count += 1
    else:
        break
print(count)