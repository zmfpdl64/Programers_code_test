# 6시 17분 6시
# 실버2

a = list(input().replace('()','R'))
stack = []
idx = 0
sep = 0
while len(a) != 0:
    str1 = a.pop(0)
    if str1 == 'R':
        if len(stack) != 0:
            num = str(stack[-1])
            if num.isdigit():
               stack[-1] = int(num) + 1
            else:
                stack.append(1)
    elif str1 == '(':
        stack.append('(')
    elif str1 == ')':
        num = stack[-1]
        if len(stack) >= 3:
            num2 = str(stack[-3])
            if num2.isdigit():
                stack[-3] += stack[-1]
                stack.pop()
                stack.pop()
            else:
                stack.pop(len(stack)-2)
        else:
            stack.pop(len(stack)-2)
        sep += num +1

print(sep)


