#11시 15분 13시
# 실버3
import sys
def solution1():
    input = sys.stdin.readline
    n = int(input())
    a = []
    result = []
    def dfs(li, idx):
        if idx < n:
            result.append(sum(li))
        elif idx == n:
            result.append(sum(li))
            return
        else:
            return
        for j in range(idx, len(a)):
            st = a[j][0]
            sv = a[j][1]
            li.append(sv)
            dfs(li, j+st)
            li.pop()
        return
    for i in range(n):
        a.append(list(map(int ,input().split())))
    for i in range(len(a)):
        dfs([], i)
    print(max(result))

def solution2():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = [0] * (n+1)

    for i in range(n-1, -1, -1):
        if i+a[i][0] > n:
            b[i] = b[i+1]
        else:
            b[i] = max(a[i][1]+b[i+a[i][0]], b[i+1])
    print(b[0])

solution2()