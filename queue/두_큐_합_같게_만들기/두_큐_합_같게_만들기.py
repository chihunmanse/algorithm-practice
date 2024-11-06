from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(q1), sum(q2)
    total_sum = sum_q1 + sum_q2
    
    if total_sum % 2 != 0:
        return -1
    
    target_sum = total_sum // 2
    count, limit = 0, len(q1) * 3
    
    while sum_q1 != target_sum:
        if count > limit:
            return -1
        
        if sum_q1 > target_sum:
            value = q1.popleft()
            sum_q1 -= value
            sum_q2 += value
            q2.append(value)
        else:
            value = q2.popleft()
            sum_q2 -= value
            sum_q1 += value
            q1.append(value)
        
        count += 1
    
    return count