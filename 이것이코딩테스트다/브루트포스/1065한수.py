#10시 48분 11시 05분
# 실4

n = int(input())
if n < 100:
    print(n)
    quit()
else:
    count = 99
    for i in range(100, n+1):
        if i//100 + i%10 == i%100//10*2:
            count +=1
print(count)






# 1 부터 99까지
# 99 +
# 111
# 123
# 135
# 147
# 159
# 210