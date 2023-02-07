a = input()
cnt = 0
answer = 0
for i, v in enumerate(a):
    if v == '(':
        cnt += 1
    else:
        cnt -= 1
        if a[i-1] == ')':
            answer += cnt
        else:
            answer += 1
print(answer)

