# 20시 06분 20시 20분
# 브2
# https://www.acmicpc.net/problem/11328
def solution1():
    n = int(input())
    for i in range(n):
        str1, str2 = map(list, input().split())
        str1.sort()
        str2.sort()
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                print("Impossible")
                break

        else:
            print("Possible")

