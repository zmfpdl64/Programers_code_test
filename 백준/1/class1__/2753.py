#10시 56분 윤년 11시 성공

a = int(input())

if a % 400 == 0:
    print(1)
elif a % 100 == 0:
    print(0)
elif a % 4 == 0:
    print(1)
else:
    print(0)