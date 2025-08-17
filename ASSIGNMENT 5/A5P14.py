def maxValue(events, k):
    events.sort(key=lambda x: x[0])
    n = len(events)
    dp = [[-1] * (k + 1) for _ in range(n)]
    def findMaxValue(index, k_left):
        if k_left < 1 or index >= n:
            return 0
        if dp[index][k_left] != -1:
            return dp[index][k_left]

        
        skip_event = findMaxValue(index + 1, k_left)

        
        next_index = findNextStart(events, index + 1, events[index][1])
        attend_event = events[index][2]
        if next_index != -1:
            attend_event += findMaxValue(next_index, k_left - 1)

        
        dp[index][k_left] = max(skip_event, attend_event)
        return dp[index][k_left]

    return findMaxValue(0, k)


def findNextStart(events, left, key):
    
    right = len(events) - 1
    answer = -1
    while left <= right:
        mid = left + (right - left) // 2
        if events[mid][0] > key:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
events = [[1,2,4], [3,4,3], [2,3,10]]
k = 2
print(maxValue(events, k))  
