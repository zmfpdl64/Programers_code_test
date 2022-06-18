#"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"
b = list()
a = int(input())
answer = list()
for i in range(a):
    b.append(input().split()) 

for i in range(a):
    result = ""
    for j in range(len(b[i][1])): #반복 선택할 문자 하나 선택
        result += b[i][1][j] * int(b[i][0])
    answer.append(result)        

for i in range(len(result)):
    print(result[i])