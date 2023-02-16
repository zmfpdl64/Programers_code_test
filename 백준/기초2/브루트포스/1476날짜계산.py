# 5시 39분 17시 55분
# 실5

e, s, m = map(int, input().split())
i = 1
while True:
    if (i-e)%15==0 and (i-s)%28==0 and (i-m)%19==0:
        print(i)
        break
    i+=1
