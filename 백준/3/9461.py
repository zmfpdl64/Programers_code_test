#12시 30분 12시 56분 26분
#1초 128MB  1<= N <= 100

a=[0,1,1,1,2,2];b=[]
for i in range(int(input())):b.append(int(input()))
for i in range(6,max(b)+1):a.append(a[i-5]+a[i-1])
for i in b:print(a[i])

