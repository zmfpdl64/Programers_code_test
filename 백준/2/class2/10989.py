#2시30분 
n = int(input())
dic = {i : 0 for i in range(1, 10001)}
for i in range(n):
    a = int(input())
    dic[a] += 1

#print('\n\n\n')
for i in range(1,10001):
    for j in range(dic[i]):
        print(i)
