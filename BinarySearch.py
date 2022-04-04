"""
Binary search works only on a sorted collection of elements

Initialize 2 pointers, .start at beginning of array, end at the end of the array. 
Find the element at the middle of the 2 pointers
If element at the middle is bigger than our goal, set end pointer to middle.
If element at the middle is smaller than our goal, set start pointer to middle + 1
"""

def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while(left <= right):
        mid = (left+right)//2 
        if arr[mid] == target:
            return mid
        elif(arr[mid] < target):
            left = mid + 1
        else:
            right = mid + 1
    
    return -1

arr = [1,2,3,4,5,6]
target = 6

result = binarySearch(arr, target) # return index

if result != -1:
    print("Element is present at index %d", result)
else:
    print("Element is not present in the array")