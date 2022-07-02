# 21시 37분 22시 15분
#1 2 3 4 5 6 7
n = int(input())
a = []
for i in range(1667):
    for j in range(1001):
        if i*3+j*5 == n:
            a.append(i+j)

print(min(a))





# sum = (n // 30) * 6
# n = n % 30
# if n == 1 or n == 2 or n == 4 or n== 7 or n == 14:
#     print(-1)
# elif n== 5 or n == 10 or n == 15 or n == 20 or n == 25:
#     sum += (n / 5)
# elif n==3 or n == 6 or n == 9 or n == 12:
#     sum += (n / 3)
# elif n== 8:
#     sum += 2
# elif n == 11 or n == 13 or n == 16:
#     sum += 3
# elif n == 18:
#     sum += 4
# elif n == 17 or n == 19 or n == 21 or n == 23:
#     sum += 5
# elif n == 22 or n == 24 or n == 26 or n == 28:
#     sum += 6
# elif n == 27 or n == 29:
#     sum += 7


# print(int(sum))














# a = n
# if (str(n)[-1] == "1"  or str(n)[-1] == "6") and n > 10:
#     n -= 6
#     mi = n // 5 + 2
#     print(mi)
# elif (str(n)[-1] == "2" or str(n)[-1] == "7") and n > 10:
#     n -= 12
#     mi = n // 5 + 4
#     print(mi)
# else:
#     mi = n // 5
#     n = n % 5
#     mi += n // 3
#     n = n % 3
#     if n == 0 :
#         print(mi)
#     else:
#         if a % 3 == 0:
#             print(a // 3)
#         else:
#             print(-1)