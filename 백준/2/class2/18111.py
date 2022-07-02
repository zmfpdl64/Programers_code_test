#19시 51분 시작
#마인크래프트
#조건 1초 1024MB
#조건 500 , 6.4 * 10^7

#최대한 빠르게 땅의 높이를 고르게 한다.
#파냐 덮냐 2  1    비교하기
#높이 비교
#보유한 블록이 존재하냐
#비교하기 위한 데이터 형식 

#1. 최대 높이 구하기 -> 최대를 채울 수 있는가?

n, m, b = map(int, input().split()) # 세로, 가로, 보유 불럭
a = []  # 지도 배열
for i in range(n):
    a += map(int, input().split())
aveg = int((sum(a)+ b) / (n*m))
mini = 100000000
height = 0
for i in range(aveg+1): #최대 높이부터 0까지
    temp = 0
    for j in a:    #보드 높이 계산
        dif = i - j
        if dif >= 0:
            temp += dif
        else:
            temp += abs(dif)*2
    if  mini >= temp:   #크거나 같다 표시를 해야하는데 크다 표시를 해서 통과되지 않았다.
        mini = temp
        height = i
print(mini, height)


# n, m, b = map(int, input().split()) # 세로, 가로, 보유 불럭
# a = []  # 지도 배열

# answer = []
# for i in range(n):
#     a.extend(list(map(int, input().split())))
# end = max(a)    # 보드 최대 높이
# c = [b] * (end +1)   # 사용할 수 있는 블록
# for i in range(end, -1, -1): #최대 높이부터 0까지
#     up = 0
#     down = 0
#     for j in range(n*m):    #보드 높이 계산
#         dif = i - a[j]
#         if dif >= 0:
#             up += dif
#             c[i] -= dif
#         else:
#             down += abs(dif)
#             c[i] += abs(dif)
#     if c[i] >= 0:
#         answer.append([up + down*2, i])
# answer = list(sorted(answer, key=lambda x : (x[0], -x[1])))
# print(answer[0])