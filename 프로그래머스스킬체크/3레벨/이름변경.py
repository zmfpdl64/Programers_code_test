
        
        dfs(map, target, words, col.pop(0), mini)
    if len(col) == 0:
        return 

def solution(begin, target, words):
    map = [False] * len(words)
    mini = []
    dfs(map, target, words, begin, mini)
    
    return answer


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])