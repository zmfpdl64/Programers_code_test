# 16시 39분

# 시간 제한 2초
# ArrayList를 이용한 문제 풀이

n = int(input())
queue = [i for i in range(1, n + 1)]
size = n
idx = 0
while (idx+1 != size):
    # 1, 2, 3, 4, 5, 6
    idx += 1
    # 2, 3, 4, 5, 6
    queue.append(queue[idx])
    size += 1
    idx += 1
    # 3, 4, 5, 6, 2
print(queue[-1])