# 15시 18분
# 브2
# https://www.acmicpc.net/problem/2750

# n개의 수가 주어졌을 때 `오름차순` 으로 정렬하라
import sys
def solution1():
    input = sys.stdin.readline
    n = int(input())
    ans = []
    # 입력값 반복해서 받기
    for i in range(n):
        num = int(input())
        ans.append(num)
    for i in range(n):
        for j in range(i, n):
            if ans[i] > ans[j]:
                ans[i],ans[j] = ans[j], ans[i]
    for i in ans:
        print(i)

def solution2():
    input = sys.stdin.readline
    n = int(input())
    ans = [0] * 2001
    # 입력값 반복해서 받기
    for i in range(n):
        num = int(input())
        ans[num] += 1
    for i in range(2001):
        if ans[i - 1000] != 0:
            print((i - 1000))

solution2()
