from collections import deque
import math

def solution(progresses, speeds):
    result = []
    queue = deque()
    
    for progress, speed in zip(progresses, speeds):
        remaining_work = 100 - progress
        remaining_day = math.ceil(remaining_work / speed)
        queue.append(remaining_day)

    while queue:
        count = 1
        current_day = queue.popleft()
        
        while queue and queue[0] <= current_day:
            queue.popleft()
            count += 1
        
        result.append(count)
    
    return result
        
        