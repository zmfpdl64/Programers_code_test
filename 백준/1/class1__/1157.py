#11시 6분 시작 11 47분 끝
a = input().lower()
b = dict()
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
maxi = max(b.values())
count = 0
answer = ""
print(maxi)
for i, v in b.items():
    print(i, v)
    if v == maxi:
        count += 1
        answer = i
    if count == 2:
        answer = "?"
        break
print(answer.upper())
    
        
    


    