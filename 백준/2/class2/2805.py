#17시 11분
#나무 자르기

import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(a)

while start <= end:
    mid = (start + end) // 2
    get_tree = 0
    for i in range(n):
        if a[i] > mid:
            get_tree += a[i] - mid
    if get_tree >= m:
        start = mid +1
    else:
        end = mid - 1
print(end)
    
#def solution(start, end, result_list):
#     mid = (start + end) // 2
#     get_tree = 0
#     for i in range(n):
#         rem = a[i] - mid
#         if rem > 0:
#             get_tree += rem
#     if get_tree >= m:
#         start = mid +1
#         result_list.append(mid)
#     else:
#         end = mid -1
#     solution(start, end, result_list)

# solution(start, end, result_list)
# print(max(result_list))
