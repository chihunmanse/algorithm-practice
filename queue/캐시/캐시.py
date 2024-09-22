from collections import deque

def solution(cacheSize, cities):
    CACHE_HIT = 1
    CACHE_MISS = 5
    
    if cacheSize == 0:
        return len(cities) * CACHE_MISS
    
    time = 0
    cache = deque([])
    
    for city in cities:
        lower_city = city.lower()
        
        if lower_city in cache:
            time += CACHE_HIT
            
            cache.remove(lower_city)
            cache.append(lower_city)
        else:
            time += CACHE_MISS
            
            if len(cache) == cacheSize:
                cache.popleft()
                
            cache.append(lower_city)
            
    return time
        
            
        