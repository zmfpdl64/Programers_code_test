#6시 56분
import math
a = list(map(int, input().split()))

i = (-a[1] + a[2]) / (a[0] - a[1])

i = math.ceil(i)
print(i)

