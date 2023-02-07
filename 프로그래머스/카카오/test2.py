#1. 가장 먼 곳 부터 해치우기 and (가져오는 양 == cap or 가져가는양 == cap)
#2. 

def solution(cap, n, deliveries, pickups):
    
    answer = -1
    c = 0
    d_sum = sum(deliveries)
    p_sum = sum(pickups)


    while d_sum != 0 and p_sum:
        p_cap = 0
        d_cap = 0
        p_idx = 0
        d_idx = 0
        for i in range(len(deliveries)-1, -1, -1):
            d_cap += deliveries[i]
            p_cap += pickups[i]
            if d_cap >= cap or p_cap >= cap:
                p_idx = i
                d_idx = i
            else:
                deliveries[i]
                

            




    sum 

    return answer