n = int(input())
network = int(input())

vi_map = [False] * (n+1)

count = 0
a = [[] for i in range(n+1)]
queue = []
# 컴퓨터가 서로 연결되어 있는 정보 자료구조
for i in range(network):
    x,y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

queue += a[1]
vi_map[1] = True

# 1 : [2, 5]
# 2 : [1, 3, 5]
# 3 : [2]
# 4 : [7]
# 5 : [1, 2, 6]
# 6 : [5]
# 7 : [4]

while len(queue) != 0:
    value = queue.pop(0)

    if not vi_map[value]:
        vi_map[value] = True
        count +=1
        queue += a[value]

print(count)