# 12시 12분 12시 56분 44분
n = int(input())
def divString(ins):
    for i in range(1, 11):
        lists = []
        for j in range(0, 30//i-1):
            lists.append(ins[i*j:i*(j+1)])
        for j in range(1, len(lists)):
            if lists[j] == lists[j-1]:
                pass
            else:
                break
            if j == len(lists)-1 :
                return i
    return -1
def printOut(idx, value):
    print("#",idx," ",value, sep="")
for i in range(n):
    ins = input().rstrip()
    value = divString(ins)
    printOut(i, value)