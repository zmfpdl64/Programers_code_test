str1 = input().replace('>', '>S').replace('<', 'S<').split('S')
answer = ''
for i in str1:
    if '<' in i:
        answer += i
    else:
        words = i.split(' ')
        words = [word[::-1] for word in words]
        answer += ' '.join(words)
print(answer)

