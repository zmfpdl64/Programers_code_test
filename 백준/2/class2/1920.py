#14시 56분 15시 50분 #이분탐색

import sys

def binary_search(target, start, end, stack):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if stack[mid] == target:
        return mid
    elif stack[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(target, start, end, stack)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()
for i in range(len(b)): #여기서 b가 아니라 a로 설정해서 자꾸 틀렸다.
    idx = binary_search(b[i], 0, len(a)-1, a)
    if idx == None:
        print(0)
    else:
        print(1)

#