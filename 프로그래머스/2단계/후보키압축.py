# https://school.programmers.co.kr/learn/courses/30/lessons/42890?language=python3
from itertools import combinations


def solution(relation):
    n_row = len(relation)  # 릴레이션의 행 수
    n_col = len(relation[0])  # 릴레이션의 열 수

    # 모든 열 조합 구하기
    cols = range(n_col)
    candidates = []
    for i in range(1, n_col + 1):
        for combination in combinations(cols, i):
            candidates.append(combination)

    # 유일성 검사
    unique = []
    for candidate in candidates:
        temp = [tuple(row[col] for col in candidate) for row in relation]
        if len(set(temp)) == n_row:
            unique.append(candidate)

    # 최소성 검사
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if set(unique[i]).issubset(set(unique[j])):
                answer.discard(unique[j])

    return len(answer)

a = set()
a.issubset()
print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

))