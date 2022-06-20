n = int(input())
stack = list()
a= list()
def func(stack, c, d = 0):
    if c == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c == "size":
        print(len(stack))
    elif c == "push":
        stack.append(d)
    elif len(stack) == 0:
        print(-1)
    elif c == "pop":
        print(stack.pop(0))
    elif c == "front":
        print(stack[0])
    elif c == "back":
        print(stack[-1])


for i in range(n):
    b = input().split()
    a.append(b)

for i in range(len(a)):
    if len(a[i]) == 2:
        func(stack, a[i][0], a[i][1])
    else:
        func(stack, a[i][0])
        

