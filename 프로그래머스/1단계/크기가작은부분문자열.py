def solution(t, p):
    size = len(p)
    count = 0
    for i in range(len(t)-size):
        num = int(''.join(t[i:i+size]))
        if num <= int(p):
            count += 1
solution('3141592', '271')