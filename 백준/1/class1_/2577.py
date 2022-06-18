#17시 04분 시작  #17시 14분 완
dic = {str(i) : 0 for i in range(10)}
sum = 1
for i in range(3):
    sum *= int(input())
sum = str(sum)
print( dic)
for i in sum:
    dic[i] += 1

for i, v in dic.items():
    print(dic[i])
