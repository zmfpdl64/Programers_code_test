# 18시 36분
# 골 5
# https://www.acmicpc.net/problem/24062

import sys
input = sys.stdin.readline
answer = 0
idx = 0
n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# arr = [5, 4, 1, 3, 2]
# arr2 = [5, 4, 1, 3, 2]
# arr2 = [1, 2, 3, 5, 4]
# arr2 = [1,4,5,3,2]
for i in range(len(arr)):
    if arr[i] != arr2[i]:
        break
else:
    print(1)
    sys.exit()
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global idx
    i = p
    j = q + 1
    tmp = [0] * (r - p + 1)
    t = 0

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1
    for i in range(p, r + 1):
        if A[i] != tmp[i-p]:
            A[i] = tmp[i - p]
            if i < idx:
                print(0)
                sys.exit()
        for j in range(idx, len(A)):
            if A[j] == arr2[j]:
                idx += 1
            else:
                break
        else:
            print(1)
            sys.exit()

merge_sort(arr, 0, len(arr)-1)
print(0)

