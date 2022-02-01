import heapq

def solution(pb) :
    print(heapq.heapify(pb))
    #print(type(pb))
    p = heapq.heappop(pb)
    while pb :
        print(p, pb)
        if p==pb[0][:len(p)] : 
            return False
        p = heapq.heappop(pb)
    
    return True
            


solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])
