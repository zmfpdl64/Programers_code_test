n = int(input())
data = [*input()]
nums = [int(input()) for _ in range(n)]
stack = []

for i in data:
    print(stack)
    if i in ['/', '*', '-', '+']:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(eval(f'{num2}{i}{num1}'))
    else:
        stack.append(nums[ord(i) - ord('A')])
print('%.2f' %stack[-1])