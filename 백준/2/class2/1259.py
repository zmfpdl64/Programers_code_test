answer = list()
a = input()
while a != "0":
    if a == a[::-1]:
        answer.append("yes")
    else:
        answer.append("no")
    a = input()

for i in range(len(answer)):
    print(answer[i])
