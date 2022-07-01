#14시 35분
#랜선 자르기
#100만 이상          메모리 제한 128MB
#2초 제한 시간    
#다시 풀어보기
import sys


a = list(map(int, input().split()))
b = []
for i in range(a[0]):
    b.append(int(sys.stdin.readline()))
line_length = 0
line_length_list = []
line_cnt = 0

start, end = 1, max(b)
while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in b:
        line += i //mid
        line_length = mid
    if line >= a[1]:
        start = mid + 1
        line_cnt = line
    else:
        end = mid - 1
        line_cnt = line
    if line_cnt >= a[1]:
        line_length_list.append(line_length)

print(max(line_length_list))
    

# print(i)

# def binary_search(c, d):
#     sum1 = 0
#     print(c, d)
#     for j in range(len(b)):
#         sum1 += b[j] // (c + d)
#     if sum1 == a[1]:
#         answer = c + d
#         return answer
#     elif sum1 > a[1]:
#         inc =  abs(c//2)
#         return binary_search(inc, c+d)
#     elif sum1 < a[1]:
#         dec = -abs(c // 2)
#         return binary_search(dec, c+d)

# i = sum(b)//a[1] #최대 길이
# answer = binary_search( i//2 , i)