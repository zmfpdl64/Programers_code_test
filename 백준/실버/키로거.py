# 실2
# https://www.acmicpc.net/problem/5397

import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    ins = list(input().rstrip())
    l_list = []
    r_list = []
    for i in ins:
        if i == '>':
            if r_list:
                l_list.append(r_list.pop())
        elif i == '<':
            if l_list:
                r_list.append(l_list.pop())
        elif i == '-':
            if l_list:
                l_list.pop()
        else:
            l_list.append(i)
    print(''.join(l_list + r_list[::-1]))