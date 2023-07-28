# 19시 54분 20시 3분
# 브2
# https://www.acmicpc.net/problem/13300
# n 참가인원, k 방최대인원
# 여자 0 남자 1
import math
# 입력값 받기
n, k = map(int, input().split())
result = 0
# (성별, 학년) : 인원      map 자료형 만들기
maps = {}
for i in range(n):
    gender, grade = map(int, input().split())
    # key 만들기
    row = (gender, grade)
    if row not in maps:
        maps[row] = 1
    else:
        maps[row] += 1
# 방 갯수 구하기
for i in maps.values():
    result += math.ceil(i/k)

print(result)

