# 16시 30분
# 실 4
# https://www.acmicpc.net/problem/10866
import sys
input = sys.stdin.readline
# deque 양방향 queue 자료구조 만들기

n = int(input())
dq = []
for i in range(n):
    ins = input().rstrip().split()
    if len(ins) == 2: # push일 때 2가지 케이스
        op = ins[0]
        if op == "push_front":
            dq.insert(0, ins[1])
        else:
            dq.append(ins[1])
    else:
        op = ins[0]
        result = 0
        try:
            if op == "pop_front":
                result = dq.pop(0)
            elif op == "pop_back":
                result = dq.pop()
            elif op == "front":
                result = dq[0]
            elif op == "back":
                result = dq[-1]
            elif op == "size":
                result = len(dq)
            elif op == "empty":
                if len(dq):
                    result = 0
                else:
                    result = 1
        except:
            result = -1
        print(result)

