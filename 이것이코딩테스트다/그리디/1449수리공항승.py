#2시 23분 2시 30분
import sys
input = sys.stdin.readline
n, l = map(int, input().split())
leak_point = list(map(int, input().split()))
leak_point.sort()
count = 0
water_map = [True] * (max(leak_point) + 1)
for i in leak_point:
    water_map[i] = False

for i in leak_point:
    if water_map[i] == False:
        count += 1
        try:
            for j in range(i, i+l):
                water_map[j] = True
        except:
            continue
print(count)

