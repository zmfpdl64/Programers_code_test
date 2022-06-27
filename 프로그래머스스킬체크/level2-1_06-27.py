def solution(bridge_length, weight, truck_weights):
    i =0
    answer = 0
    go_bridge = []
    time = []
    while i >= 0:
        i += 1
        if len(time) != 0 and time[0] == i:
            go_bridge.pop(0)
            answer = time.pop(0)
        if   len(truck_weights) != 0  and weight >= (sum(go_bridge)+ truck_weights[0]):
            time.append(i+ bridge_length)
            go_bridge.append(truck_weights.pop(0))
        
        
        if len(go_bridge) == 0 and len(truck_weights) == 0:
            return answer


solution(2, 10 ,[7,4,5,6])