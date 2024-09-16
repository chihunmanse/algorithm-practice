def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, price in enumerate(prices):
        while stack and (prices[stack[-1]] > price or i == len(prices) - 1):
            index = stack.pop()
            answer[index] = i - index
            
        stack.append(i)
    
    return answer