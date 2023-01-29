def main():
    t = int(input())

    for i in range(t):
        case = list(map(int, input().split()))
        solution(case)



def solution(case):
    b = list()
    index = 0
    for i in range(1, len(case)+1):
        b.append([i * 2 + abs(i - case[i]), i])







if __name__ == "__main__":
    main()
