from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)
    time = 0
    current_weight = 0
    
    for truck in truck_weights:
        while True:
            time += 1
            current_weight -= queue.popleft()
            
            if truck + current_weight <= weight:
                queue.append(truck)
                current_weight += truck
                break
            else:
                queue.append(0)
    
    return time + bridge_length
    