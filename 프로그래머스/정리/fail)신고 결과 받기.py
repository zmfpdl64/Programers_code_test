a= ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
b = ["muzi", "frodo", "apeach", "neo"]
d = ["ryan con", "ryan con", "ryan con", "ryan con"]
c = {}  #신고한사람
k = 2
cp = {} #총 받은 수
for i in range(len(b)): #사용자 dict 생성
    c[b[i]] =''
    cp[b[i]] = 0
for i in range(len(a)): #사용자 신고
    a[i] = a[i].split(' ')

for i in range(len(b)): #사용자 신고 모음
    for j in range(len(a)):
        if a[j][0] == b[i]:
            c[b[i]] += a[j][1] + ' '
for i in range(len(b)):
    c[b[i]] = c[b[i]].strip().split(' ')    #리스트화
for i in range(len(b)): #중복 제거
    c[b[i]] = set(c[b[i]])
    c[b[i]] = list(c[b[i]])

e = []
g = 0
for i in range(len(b)): #사람별 신고 받은 횟수
    for j in range(len(b)):
        for h in range(len(c[b[j]])):
            if b[i] == c[b[j]][h]:
                cp[b[i]] += 1
answer= []
re = 0
for i in range(len(b)): #정지 이용자
    if cp[b[i]] >= k:
        e.append(b[i])
for i in range(len(b)):
    for j in range(len(c[b[i]])):
        for h in range(len(e)):
            if c[b[i]][j] == e[h]:
                re += 1
    answer.append(re)
    re = 0
                
        
print(cp)
print(answer)
print(e)




