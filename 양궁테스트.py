d = [6.667, 9.0, 8.0, 7.0, 6, 5, 4, 3, 2, 1, 0]
e = [2,1,1,1,0,0,0,0,0,0,0]
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
g = [0] * len(d)
answer = [0] * len(d)
n = 5
score1 = 0
score2 = 0
dic = { ind : val for ind, val in enumerate(d)}
print(dic)
dic = sorted(dic.items(), key=(lambda x: x[1]), reverse =True)
dic = dict(dic) #sorted함수를 사용하면 tuple로 바뀌기 때문에 dict를 해줘야한다.
print(dic)
for i in dic:
    if n >= e[i]+1 and n != 0:
        g[i] += e[i]+1
        n -= e[i]+1
        score1 += dic[i]
        e[i] = 0
for i in range(len(e)):
    if e[i] != 0:
        score2 += max(a) - i


if score1 <= score2:
    print('이길방법이 없습니다...')
#    return [-1]

print(g)
#return g

    
