#10시 02분 시간초과 그래서 에라토스테네스의 체 이용
a = []
b = list(map(int, input().split()))
n = b[1] + 1
c = [True] * n

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
m = int(n ** 0.5)
for i in range(2, m + 1):
    if c[i] == True:           # i가 소수인 경우
        for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
            c[j] = False

for i in range(b[0], n):
    if i == 1:
        pass
    elif c[i] == True:
        a.append(i)

for i in range(len(a)):
    print(a[i])













# for i in range(2, m+1):
#     if c[i] == True:
#         for j in range(i+i, b[1], i):
#             c[j] = False


# for i in range(b[0],b[1]+1):
#     if i == 1:
#         pass
#     elif c[i] == True:
#         a.append(i)

# for i in range(len(a)):
#     print(a[i])
