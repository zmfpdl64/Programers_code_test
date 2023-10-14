# 14시 32분 14시 38분
# 브 2
# https://www.acmicpc.net/problem/5585

answer = 0
ins = 1000 - int(input())

mod_m = [500, 100, 50, 10, 5, 1]
for i in mod_m:
    answer += ins // i
    ins %= i
print(answer)
