# 19시 38분 20시 53분
# 실5
# https://www.acmicpc.net/problem/1475
import math
# 0부터 9까지 배열 생성
a = [0] * 10
for i in map(int, list(input().rstrip())):
    # 들어온 idx 에 + 1
    a[i] += 1
maxi = 0
for i in range(len(a)):
    # 6, 9 를 제외한 최댓값 계산
    if i != 6 and i != 9:
        maxi = max(maxi, a[i])
# 6, 9의 갯수를 더하고 2로 나누어 올림한 값과 최댓값과 비교
maxi = max(maxi, (a[6]+a[9])/2)
print(math.ceil(maxi))

