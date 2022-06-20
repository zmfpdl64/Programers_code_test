#2시30분 
import time, random
start = time.time()
N = 1000000

N_list = [0] * 10001

for _ in range(N):
    data = random.randint(1, 10000)
    N_list[data] += 1

for i in range(10001):
    if N_list[i] != 0:
        for j in range(N_list[i]):
            print(i)