#1시 34분 1시 52분
#rstrip('\n') 때문에 시간이 상당히 걸림
# 브2
import sys
input = sys.stdin.readline
while True:
    str1 = input().rstrip('\n')
    if not str1:
        break
    sep = [0, 0, 0, 0]
    for i in str1:
        if i.islower():
            sep[0] += 1
        elif i.isupper():
            sep[1] += 1
        elif i.isdigit():
            sep[2] += 1
        elif i.isspace():
            sep[3] += 1
    print(*sep)
