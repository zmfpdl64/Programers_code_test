from collections import deque as d

def solution(queue1, queue2):
    count = 0
    len1 = len(queue1) + len(queue2)
    queue1 = d(queue1)
    queue2 = d(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    while q1_sum != q2_sum:
        if q1_sum == 0 or q2_sum == 0 or count >=len1:
            return -1
        if q1_sum < q2_sum:
            q_sub = queue2.popleft()
            queue1.append(q_sub)
            q1_sum += q_sub
            q2_sum -= q_sub
        else:
            q_sub = queue1.popleft()
            queue2.append(q_sub)
            q1_sum -= q_sub
            q2_sum += q_sub
        count += 1
        
    return count

print(solution([3,2,7,2], [4,6,5,1]))