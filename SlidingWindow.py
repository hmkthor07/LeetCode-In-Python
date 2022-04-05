"""
Given an array of integers of size N, find maximum sum of K consequtive elements.
"""

# Brute Force

def maxSum_bf(arr, k):
    max_num = float('-inf')
    n = len(arr)

    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+j]

        max_num = max(current_sum, max_num)

    return max_num

# Sliding window

def maxSum(arr, WindowSize):
    arraySize = len(arr)
    if arraySize <= WindowSize:
        print('Invalid Operation')
        return -1
    
    window_sum = sum([arr[i] for i in range(WindowSize)])
    max_sum = window_sum

    for i in range(arraySize - WindowSize):
        window_sum = window_sum - arr[i] + arr[i + WindowSize]
        max_sum = max(window_sum, max_sum)

    return max_sum

arr = [80, -50, 90, 100]
k = 2
answer = maxSum(arr, k)
print(answer)