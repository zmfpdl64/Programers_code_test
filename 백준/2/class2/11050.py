#6시33분 6시 40분
import itertools

from requests import head
a = list(map(int, input().split()))

arr = [i for i in range(a[0])]

result =list(itertools.combinations(arr, a[1]))
print(len(result))
