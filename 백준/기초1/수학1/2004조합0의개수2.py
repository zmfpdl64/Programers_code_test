n, m = map(int, input().split())
n, m = max(n, m), min(n, m)
nm = max(n-m, m)

def twocount(num1):
    count = 0
    while num1 != 0:
        num1 = num1 //5
        count += num1
    return count

def fivecount(num1):
    count = 0
    while num1 != 0:
        num1 = num1 // 5
        count += num1
    return count

print(min(twocount(n) - twocount(m) - twocount(nm), fivecount(n) - fivecount(nm) - fivecount(m)))

