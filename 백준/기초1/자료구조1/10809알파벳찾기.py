#1시31분 1시 33분
# 브5
a = [-1] * 26
str1 = input().rstrip()
for i in str1:
    a[ord(i)-ord('a')] = str1.index(i)
print(*a)