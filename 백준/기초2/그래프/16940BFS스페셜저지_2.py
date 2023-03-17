import sys
input = sys.stdin.readline
N = int(input())
tree = {i:[] for i in range(1,N+1)}
tree[0] = [1]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a] += [b]
    tree[b] += [a]
seqs = list(map(int,input().split()))
que=[0]
idx=0
for num in seqs:
    while num not in tree[que[idx]]:
        idx+=1
        if idx == len(que):
            print(0)
            exit()
    que.append(num)
print(1)