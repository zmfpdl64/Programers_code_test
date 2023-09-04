# 21시 26분
# 실5
# https://www.acmicpc.net/problem/24174

n, m = map(int, input().split())
a = list(map(int, input().split()))

def heap_sort(A):
  build_min_heap(A)
  for i in range(len(A) - 1, 1, -1):
    A[1], A[i] = A[i], A[1]
    heapify(A, 1, i - 1)

def build_min_heap(A):
  for i in range(int(len(A) / 2), 0, -1):
    heapify(A, i, len(A))

def heapify(A, k, n):
  left = 2 * k
  right = 2 * k + 1
  smaller = left if left <= n and A[left] < A[right] else right
  if smaller <= n and A[smaller] < A[k]:
    A[k], A[smaller] = A[smaller], A[k]
    heapify(A, smaller, n)