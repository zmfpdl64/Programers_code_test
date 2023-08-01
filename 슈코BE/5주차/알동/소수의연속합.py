# 14시 38분 14시 58분
# 골 3
# https://www.acmicpc.net/problem/1644


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def eratosthenes(n):
    bool_map = [False, True] + [True] * (n-1)
    prime_map = []
    for i in range(2, n+1):
        if bool_map[i]:
            prime_map.append(i)
            for j in range(i*2, n+1, i):
                bool_map[j] = False
    return prime_map
def create_prime_map(n):
    prime_map = [2]
    for i in range(3, n+1):
        if is_prime(i):
            prime_map.append(i)
    return prime_map
n = int(input())
prime_map = eratosthenes(n)
count = 0
if prime_map:
    start = 0
    end = 0
    sum1 = prime_map[0]
    while end < len(prime_map):
        if sum1 > n:
            sum1 -= prime_map[start]
            start += 1
        elif sum1 == n:
            sum1 -= prime_map[start]
            start += 1
            count +=1
        else:
            end += 1
            if end == len(prime_map):
                break
            sum1 += prime_map[end]
print(count)

