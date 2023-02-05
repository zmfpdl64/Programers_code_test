MAX = 1000000
prime_arr = [True]*(MAX+1)
prime_arr[0], prime_arr[1] = False, False
for i in range(2, MAX+1):
    if prime_arr[i]:
        j = i*i
        while j <= MAX:
            prime_arr[j] = False
            j += i
while True:
    n = int(input())
    if not n:
        break
    result = None
    for i in range(3, int(n/2)+1):
        if prime_arr[i] and prime_arr[n-i]:
            result = f'{n} = {i} + {n-i}'
            break
    if result:
        print(result)
    else:
        print("Goldbach's conjecture is wrong.")