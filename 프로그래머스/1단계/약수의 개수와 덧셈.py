def even(n):
    check = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            check += 1
    if check % 2 == 0:
        return 1
    else:
        return 0

def solution(left, right):
    sum1 = 0
    for i in range(left, right+1):
        if even(i):
            sum1 += i
        else:
            sum1 -= i
    return sum1


solution(13, 17)
solution(24, 27)