from collections import deque

def solution(priorities, location):
    # 우선순위 빈도 카운트
    priority_count = [0] * 10  # 우선순위는 1부터 9까지이므로 10개의 공간 생성
    for priority in priorities:
        priority_count[priority] += 1

    # 프로세스 큐 생성 (우선순위, 인덱스) 형태로 저장
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    executed_count = 0  # 실행된 프로세스 수

    for priority_level in range(9, 0, -1):  # 9부터 1까지 우선순위 확인
        while priority_count[priority_level] > 0:
            cur_priority, cur_idx = queue.popleft()
            
            if cur_priority == priority_level:
                executed_count += 1
                priority_count[priority_level] -= 1  # 해당 우선순위 처리 완료
                
                if cur_idx == location:  # 찾고자 하는 프로세스이면 실행 순서 반환
                    return executed_count
            else:
                queue.append((cur_priority, cur_idx))  # 우선순위가 낮으면 큐의 끝으로 이동
