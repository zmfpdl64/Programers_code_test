# 8시 18분 8시 28분 10분

T = int(input())
for idx in range(1, T+1):
    s = input().rstrip()
    str1 = ""
    str2 = ""
    if len(s) % 2 == 0:
        str1 = s[:len(s)/2]
        str2 = s[len(s)/2:][::-1]
    else:
        str1 = s[:len(s)//2]
        str2 = s[len(s)//2+1:][::-1]
    if str1 == str2:
        print("#{} {}".format(idx, 1))
    else:
        print("#{} {}".format(idx, 0))