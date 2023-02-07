#3시 5분 3시 25분
# 브1
a = [ chr(ord('a')+ i) for i in range(26)]
A = [ chr(ord('A')+ i) for i in range(26)]

answer = []
str1 = input()
for i in str1:
    if i.islower():
        answer.append(a[(ord(i)- ord('a')+13)%26])
    elif i.isupper():
        answer.append(A[(ord(i)-ord('A')+13)%26])
    else:
        answer.append(i)
print(''.join(answer))

