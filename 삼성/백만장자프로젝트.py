# 11시 10분 11시 57분 47분
n = int(input())
def printOut(idx, value):
    print("#",idx," ",value,  sep="")

for i in range(n):
    array_len = int(input())
    a = list(map(int,input().rstrip().split(" ")))
    a = a[::-1]
    stack =[]
    maxi = 0
    result = 0
    for j in range(len(a)):
        value = a[j]
        if value > maxi:
            while stack:
                v = stack.pop()
                result += maxi - v
            maxi = value
        stack.append(value)
    for j in stack:
        result += maxi - j
    printOut(i+1, result)

