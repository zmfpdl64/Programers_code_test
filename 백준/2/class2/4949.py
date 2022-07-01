#]로 시작하는 반례를 빠트렸다.
a = []
b = ""
while True:
    b = input()
    stack = []
    if b == ".":
        break
    for i in range(len(b)):
        if b[i] == "(":
            stack.append("(")
        elif b[i] == "[":
            stack.append("[")
        elif b[i] == "]" and len(stack) != 0 and stack[-1] == "[":
            stack.pop()

        elif b[i] == ")" and len(stack) != 0 and stack[-1] == "(":
            stack.pop()
        elif b[i] == "]":
            stack.append(b[i])
        elif b[i] == ")":
            stack.append(b[i])
        
        
    if len(stack) != 0:
        a.append("no")
    else:
        a.append("yes")
 
for i in range(len(a)):
    print(a[i])
