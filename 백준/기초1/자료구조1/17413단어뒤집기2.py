#5시 33분 6시 01분 28분걸림
# 실3
str1 = input()
answer = ''
idx = 0
word = ''
while len(str1) != idx:
    st = str1[idx]
    if st == '<':
        answer += word
        answer += st
        word = ''
        while True:
            idx += 1
            st1 = str1[idx]
            if st1 == '>':
                answer += st1
                break
            else:
                answer += st1
    elif st == ' ':
        answer += word
        word = ''
        answer += st
    else:
        word = st + word
    idx += 1
answer += word
print(answer)

d = []
print(''.join(d))