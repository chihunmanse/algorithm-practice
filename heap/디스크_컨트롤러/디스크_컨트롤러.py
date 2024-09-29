import heapq

def solution(jobs):
    # jobs를 요청 시간 순으로 정렬
    jobs.sort(key = lambda x: x[0])
    
    heap = []
    time, total_time, index, count = 0, 0, 0, len(jobs)
    
    while index < count or heap:
        # 현재 시간까지 들어온 모든 작업을 힙에 추가
        while index < count and jobs[index][0] <= time:
            heapq.heappush(heap, (jobs[index][1], jobs[index][0])) # (소요시간, 요청 시간)
            index += 1
        
        if heap:
            # 가장 소요 시간이 적은 작업부터 처리
            job_duration, job_request_time = heapq.heappop(heap)
            time += job_duration
            total_time += time - job_request_time
        else:
            # 처리할 수 있는 작업이 없으면 시간 증가
            time = jobs[index][0]
            
    return total_time // count