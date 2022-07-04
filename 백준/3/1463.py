#18시 38분 시작
#제한조건 0.15초 128MB 1<= N <= 1,000,000
#해결방법 모든 경우의 수를 대입하는 브루트 포스지만 메모리제이션을 이용해 반복되는 작업을 피했다.


n = int(input())
a = [-1] * (n+1)
def solution(n):
    global a
    if n == 1:
        return 0
    elif a[n] != -1:
        return a[n]
    else:
        if n % 3 == 0:
            a[n] = min(solution(n//3), solution(n-1))+1
        elif n % 2 == 0:
            a[n] = min(solution(n//2), solution(n-1))+1
        else:
            a[n] = solution(n-1)+1
    return a[n]
print(solution(n))