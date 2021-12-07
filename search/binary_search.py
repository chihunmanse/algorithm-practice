def bin_search(sequence, target):
    min = 0 # 검색 범위 맨 앞 인덱스
    max = len(sequence) - 1 # 검색 범위 맨 끝 인덱스

    while min <= max:
        mid = (min + max) // 2 # 중간 인덱스
        print(min, mid, max)
        if sequence[mid] == target:
            return mid # 타겟과 중간값 일치로 검색 성공
        
        elif sequence[mid] < target:
            min = mid + 1 # 타겟이 중간값보다 크면 시작값을 중간값 +1로 설정하여 검색 범위를 뒤쪽 절반으로 좁힘

        else:
            max = mid - 1 # 타겟이 중간값보다 작으면 끝 값을 중간값 -1로 설정하여 검색 범위를 앞쪽 절반으로 좁힘

    return -1

list = [1,2,3,4,5,6,7,8,9,10]
print(bin_search(list, 0))
# 0 4 9
# 0 1 3
# 0 0 0
# -1
print(bin_search(list, 3))
# 0 4 9
# 0 1 3
# 2 2 3
# 2
print(bin_search(list, 8))
# 0 4 9
# 5 7 9
# 7
print(bin_search(list, 11))
# 0 4 9
# 5 7 9
# 8 8 9
# 9 9 9
# -1

# 입국심사 문제
# 문제 설명
# n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.

# 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.

# n = 6	 times = [7, 10] return = 28
def solution(n, times):
    answer = 0
    left  = 1 # 최소시간 1분
    right = max(times) * n # 최대시간 60분
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n명 모두 심사받는 경우이다.

    while left <= right:
        mid = (left + right) // 2 
        print(left, mid, right)
        people = 0 
        # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
        for time in times: # time은 심사관 한 명 
            people += mid // time # 0 : 30 // 7 = 4  1 : 30 // 10 = 3
            if people >= n: # people = 4 / people = 7 -> 반복문 나옴
                break
        # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
        print(people)

        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid # answer = 30분
            right = mid - 1 # right = 29분 
        
        else:
            left = mid + 1 
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
    return answer

print(solution(6, [7,10]))

# 1 30 60
# 7
# 1 15 29
# 3
# 16 22 29
# 5
# 23 26 29
# 5
# 27 28 29
# 6
# 27 27 27
# 5
# 28