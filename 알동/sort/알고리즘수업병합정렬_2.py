import sys
input = sys.stdin.readline
count = 0
answer = 0
# n, m = map(int ,input().split())
# arr = list(map(int, input().split()))
m = 7
arr = [4, 5, 1, 3, 2]
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, answer
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
        count += 1
        if count == m:
            answer = tmp[i-p]
        A[i] = tmp[i - p]

merge_sort(arr, 0, len(arr)-1)
if count < m:
    print(-1)
else:
    print(answer)