a = list()
for i in range(9):
    a.append(int(input()))
maxi = max(a)
index = 0
for i in range(len(a)):
    if maxi == a[i]:
        index = i+1
print(maxi,'\n', index)
