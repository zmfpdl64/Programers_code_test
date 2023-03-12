# 17시 02분 17시 40분
# 실1
n = int(input())
a = input().split()
maxi = ''
mini = 'a'*10
vi_map = [False] * 10
def check(i, j, ch):
    if ch == '<':
        if i < j:
            return True
    else:
        if i > j:
            return True
    return False
def dfs(depth, arr):
    global mini, maxi
    if depth == n+1:
        num = ''.join(map(str, arr))
        mini = min(mini, num)
        maxi = max(maxi, num)
        return
    for j in range(10):
        if vi_map[j] == False:
            arr.append(j)
            vi_map[j] = True
            if len(arr) <= 1 :
                dfs(depth+1, arr)
            elif len(arr) >= 2 and check(arr[-2], arr[-1], a[len(arr)-2]):
                dfs(depth+1, arr)
            arr.pop()
            vi_map[j] = False
dfs(0, [])

print(maxi, mini, sep='\n')