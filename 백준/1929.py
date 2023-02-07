import sys

answer = list()

def solution(start, end):
    for i in range(start, end+1):
        if isPrime(i):
            answer.append(i)
def isPrime(num):
    if num in (0, 1):
        return False
    lim = int(num ** 0.5 + 1)
    for i in range(2, lim):
        if num % i == 0:
            return False
    return True
def printAnswer():
    for i in answer:
        print(i)

input = sys.stdin.readline
test = list(map(int, input().split()))
solution(test[0], test[1])
printAnswer()

