def solution(citations):
    citations.sort(reverse=True)
    answer = list(map(min, enumerate(citations, start=1)))
    
    print(answer)
    return answer
solution([3, 0, 6, 1, 5])