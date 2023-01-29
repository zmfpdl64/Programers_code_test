# 17시 3분 17시 28분
# 1초 128Mb  1 <= N <= 100
n = int(input())
network = int(input())
vi_map = [False] * (n+1)
count = 0
a = [[] for i in range(n+1)]
queue = []
for i in range(network):
    x,y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
queue += a[1]
vi_map[1] = True
while len(queue) != 0:
    value = queue.pop(0)
    if vi_map[value] == False:
        vi_map[value] = True
        count +=1
        queue += a[value]
print(count)
