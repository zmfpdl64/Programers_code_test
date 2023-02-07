#11시55분
# 골2

ins = input().rstrip()
op = ['+', '-', '/', '*','(']
prio = [1, 1, 2, 2, 0]
stack = []
answer = []
for i in ins:
    if i.isalpha():
        answer.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    else:
        while stack and prio[op.index(stack[-1])] >= prio[op.index(i)]:
            answer.append(stack.pop())
        stack.append(i)
while stack:
    answer.append(stack.pop())
print(''.join(answer))
