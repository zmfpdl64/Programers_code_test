# 11시 59분 12시 09분

n = int(input())
answer = []

def count369(num):
    result = 0
    arr = ["3", "6", "9"]
    num = str(num)
    for i in arr:
        result += num.count(i)
    return result


def crap(num):
    result = ""
    for i in range(num):
        result += "-"
    return result


for i in range(1, n + 1):
    num = count369(i)
    if num == 0:
        answer.append(i)
    else:
        answer.append(crap(num))
print(*answer)