#10시 53분 11시 43분

n = int(input())
answer = []
for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c= [i for i in range(len(b))]
    d = list(zip(c, b))
    count = 0
    while True:
        maxi = max(d, key=lambda x: x[1])
        if d[0][1] == maxi[1]:
            count += 1
            if d[0][0] == a[1]:
                break
            d.pop(0)
        else:
            d.append(d.pop(0))
    answer.append(count)
for i in range(len(answer)):
    print(answer[i])
        




















# n = int(input())
# answer = []
# for i in range(n):
#     a = list(map(int, input().split())) #a[0] 배열크기 a[1] 배열순서
#     b = list(map(int, input().split())) #배열들 
#     c = [ i for i in range(a[0])]
#     d = list(zip(c, b))       # 순서 : value
#     count = 0
#     while True:
#         if max(d, key=lambda x: x[1]) != d[0][1] and d[0][0] == a[0]:
#             count += 1
#             break
#         elif max(d, key=lambda x: x[1]) != d[0][1]:
#             d.append(d.pop(0))
#         else:
#             d.pop(0)
#             count += 1
#     answer.append(count)

# for i in range(len(answer)):
#     print(answer[i])