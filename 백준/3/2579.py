#1시 19분
#1초 128MB   1<= N <= 300  점수 <= 10,000
#문제 유형 파악
#계단의 점수 최댓값 구하기 -> 브루트 포스, 구현,  OR 다이나믹 프로그래밍
# 첫번째 두번째 3번째 다 구하기
#메모리제이션은 아니다
# [1], [1,2]  3칸을 띄우거나 3칸을 연속으로 이동할 수 없다.
#[ 10, 20, 15, 25, 10, 20]
#[15, 17.5, 20, 17.5, 20, 17.5, 15]
#[16.75, 18.25, 18.25, 18.25, 18.25, 16.75]
#메모리 제이션 어떻게 하는거야?
a = int(input())

stair = []
matrix = [[0] * 3 for i in range(0, a + 1)]

for i in range(0, a):
    stair.append(int(input()))

for i in range(1, a+1): 
    matrix[i][2] = max(matrix[i-1][1], matrix[i-1][0])  
    matrix[i][1] = matrix[i-1][2] + stair[i-1]          
    matrix[i][0] = matrix[i-1][1] + stair[i-1]

print(max(matrix[i][1], matrix[i][0]))



