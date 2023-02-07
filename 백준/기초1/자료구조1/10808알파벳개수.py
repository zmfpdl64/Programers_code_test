#1시29분 1시 31분
# 브4

str1 = input().rstrip()
a = [0] * 26

for i in str1:
    a[ord(i)-ord('a')] += 1

print(*a)