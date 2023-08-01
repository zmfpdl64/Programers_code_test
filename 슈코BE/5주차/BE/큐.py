# 15시 57분 16시 10분
# 실4
# https://www.acmicpc.net/problem/10845

import sys
input = sys.stdin.readline
# 시간제한0.5초  용량 256MB
# 1 <= N <= 10_000       1 <= 크기 <= 100_000  가능한 시간 복잡도 nlogn (30_000_000)

# 문제 큐 자료구조를 구현해라
# FIFO(First Input First Out)

# 메소드 push, pop, size, empty, front, back
queue = []
n = int(input())

for i in range(n):
    ins = input().rstrip().split()

    if len(ins) == 2: # push일 때만 인자가 2개
        op = ins[0]
        if op == "push": # 확실히 안정성
            queue.append(int(ins[1]))
    else:
        op = ins[0]
        result = 0
        try:
            if op == 'pop':
                result = queue.pop()
            elif op == "front":
                result = queue[0]
            elif op == "back":
                result = queue[-1]
            elif op == "size":
                result = len(queue)
            elif op == "empty":
                if len(queue) == 0:
                    result = 1
                else:
                    result = 0
        except:
            result = -1
        print(result)









