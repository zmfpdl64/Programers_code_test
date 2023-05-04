from collections import defaultdict as dd


def solution(info, query):
    answer = []
    dic = dd(lambda: [])
    for a in ["cpp", "java", "python", "-"]:
        for b in ["backend", "frontend", "-"]:
            for c in ["junior", "senior"]:
                for d in ["chicken", "pizza", "-"]:
                    dic[(a, b, c, d)] = list()

    for i in info:
        i = i.split(" ")
        for a in [i[0], "-"]:
            for b in [i[1], "-"]:
                for c in [i[2], "-"]:
                    for d in [i[3], "-"]:
                        dic[(a, b, c, d)].append(int(i[-1]))
    for i in dic.keys():
        dic[i].sort()
    for i in query:
        i = " ".join(i.split(" and "))
        i = i.split(" ")
        sc = int(i[-1])
        al = dic[tuple(i[:-1])]
        l = 0
        r = len(al)
        mid = 0
        while l < r:
            mid = (r + l) // 2
            if al[mid] >= sc:
                r = mid
            else:
                l = mid + 1
        answer.append(len(al) - l)
    return answer