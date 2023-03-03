def solution(word):
    a = ['A', 'E', 'I', 'O', 'U']
    dic = []

    def dfs(depth, st):
        if depth == 5:
            return
        for i in range(len(a)):
            dic.append(st + a[i])
            dfs(depth + 1, st + a[i])

    dfs(0, '')
    return dic.index(word) + 1