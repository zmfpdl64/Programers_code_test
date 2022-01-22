a= ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
b = ["muzi", "frodo", "apeach", "neo"]
d = ["ryan con", "ryan con", "ryan con", "ryan con"]
c = {}  #신고한사람
k = 2
e = 0
g = []
answer = []
cp = {} #총 받은 수
a = list(set(a))    #중복 제거
for i in range(len(a)): #사용자 신고
    a[i] = a[i].split(' ')

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j][1]:
            e += 1
            if e >= k:
                g.append(b[i])
    e = 0
for i in range(len(b)):
    c[b[i]] = 0

for i in range(len(a)):
    for j in range(len(g)):
        if a[i][1] == g[j]:
            c[a[i][0]] += 1
            
for i in range(len(b)):
    answer.append(c[b[i]])
print(answer)

print(c)





