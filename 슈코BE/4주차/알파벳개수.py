# 19시 34분 37분
# 브4
# https://www.acmicpc.net/problem/10808

dic = {chr(i+97) : 0 for i in range(26)}
for i in list(input().rstrip()):
    dic[i] += 1
print(*dic.values())