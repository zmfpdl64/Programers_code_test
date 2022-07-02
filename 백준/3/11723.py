#18시 00분 18시 45분
#메모리 초과, 시간초과, 
# 메모리 해결 list에 담지 않고 print함
# 시간초과 배열을 계수 배열을 이용했다.

import sys


n = int(input())
a = []
real_answer = []
b = [0] * 21
answer = [0] * 21
for i in range(n):
    a = sys.stdin.readline().split()
    if len(a) == 1:
        com = a[0]
        if com == "all":
            answer.clear()
            answer = [1] * 21
        elif com == "empty":
            answer = [0] * 21
    else:
        com = a[0]
        num = int(a[1])
        if com == "add":
            if answer[num] != 0:
                pass
            else:
                answer[num] += 1
        elif com == "remove":
            if answer[num] != 0:
                answer[num] -= 1
            else:
                pass
        elif com == "check":
            if answer[num] != 0:
                print(1)
            else:
                print(0)
        elif com == "toggle":
            if answer[num] != 0:
                answer[num] -= 1
            else:
                answer[num] += 1


# for i in range(len(a)):
#     if len(a[i]) == 1:
#         com = a[i][0]
#         if com == "all":
#             answer.clear()
#             answer = [i for i in range(1, 21)]
#         elif com == "empty":
#             answer.clear()
#     else:
#         com = a[i][0]
#         num = int(a[1])
#         if com == "add":
#             if num in answer:
#                 pass
#             else:
#                 answer.append(num)
#         elif com == "remove":
#             if num in answer:
#                 answer.remove(num)
#             else:
#                 pass
#         elif com == "check":
#             if num in answer:
#                 print(1)
#             else:
#                 print(0)
#         elif com == "toggle":
#             if num in answer:
#                 answer.remove(num)
#             else:
#                 answer.append(num)
    