#16시 23분 시작 16시 54분 클리어
#동전 0
# 1초 256MB  1 <= N <= 10 , 1 <= k <= 100,000,000
#오름 차순으로 주어짐
#문제 유형 판단하기
#BFS, DFS 아니다 그럼 그리디? 맞는거 같다.
#그럼 어떻게? 최댓값으로 나눴을 때 최소값 몫, 나머지

#해결방안
#각각 나눠서 몫을 구하고 최소 몫이랑 비교하여 
#while문 안에서 반복했다.
import sys


input = sys.stdin.readline

count = 0

remainder = 0
min_share = 0
a = []
b = []
n, money = map(int,input().split())
for i in range(n):
    a.append(int(input().rstrip()))
while money != 0:
    for i in range(len(a)):
        share = money // a[i]
        if i == 0:
            min_share = share
            remainder = money % a[i]
        if min_share >= share and share != 0:
            min_share = share
            remainder = money % a[i]
        
    money = remainder
    count += min_share
    
print(count)