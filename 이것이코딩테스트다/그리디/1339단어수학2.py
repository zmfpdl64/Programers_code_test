import sys
input = sys.stdin.readline
n = int(input())
a = [0] * 26 #알파뱃 배열 만들기
for i in range(n):
    num = list(input().rstrip())
    for i in range(len(num)):
        a[ord(num[i])-65] += 10 ** (len(num)-i-1) # 각자리마다 값 매기기
a.sort(reverse = True) # 큰값부터 정렬하기

answer = 0
num = 9
for i in a: # 큰 값부터 9부터 곱해주기
    if i == 0:
        break
    answer += i * num
    num -= 1
print(answer)