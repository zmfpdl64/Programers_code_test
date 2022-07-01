#12시 58분
n = int(input())
a = [3,6,9,2,1]
b = [3,6,9,12,6 ]
c = [1, 2, 3, 4, 2]
d = str(n)[-1]
mi = (n // 15) *3
n = n % 15
#if d in map(str,a):
try:
    index = a.index(int(d))
    if index:
        n -= b[index]
        mi += c[index]
    mi += n // 5
    n %= 5
    mi += n // 3
    n %= 3
    if n < 0 or n != 0:
        print(-1)
    else:
        print(mi)
except:
    mi += n // 5
    n %= 5
    mi += n // 3
    n %= 3
    if n < 0 or n != 0:
        print(-1)
    else:
        print(mi)
# else:
#     mi = n // 5
#     n %= 5
#     mi += n // 3
#     n %= 3
#     if n < 0 or n != 0:
#         print(-1)
#     else:
#         print(mi)  



















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