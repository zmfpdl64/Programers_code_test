# 3시 36분 3시 49분
# 실3
n = int(input())
if not n:
    print(0)
    quit()
res = ""
while n:
    if n % (-2):
        res = '1' + res
        n = n // -2 + 1
    else:
        res = '0' + res
        n = n // -2
print(res)