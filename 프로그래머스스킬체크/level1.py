def solution(strings, n):
    sorti = [ i[n] for i in strings]
    sortstring = list(zip(strings, sorti, range(0, len(strings))))
    sortstring = sorted(sortstring, key=lambda x: (x[1], x[0]))
    print(sortstring)
    answer = []
    for i in sortstring:
        answer.append(i[0])

    print(answer)
    return answer

solution(["sun", "bed", "car"], 1)
solution(["abce", "abcd", "cdx"], 2)