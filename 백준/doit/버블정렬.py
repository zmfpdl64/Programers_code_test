def bubble(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j+1], li[j] = li[j], li[j+1]
    print(*li)

bubble([3,2,1,5,4])

def select(li):
    for i in range(len(li)):
        mini_idx = i
        for j in range(i, len(li)):
            if li[mini_idx] > li[j]:
                mini_idx = j
        li[mini_idx], li[i] = li[i], li[mini_idx]
    print(*li)
select([3, 2, 1, 5, 4])
