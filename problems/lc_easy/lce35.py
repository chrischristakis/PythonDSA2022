# Search Insert Position
"""
1) Naive solution: Loop through the array and return index, or add element at x where arr[x+1] is > array
This is O(n)

2) O(log n) solution: Binary Search. find midpoint, and keep finding midpoint until we find a place to put it
Use left and right pointers to shift the midpoint, we're done when they are equal or left pointer > right pointer.
"""
def searchInsert(nums, target):
    left = 0
    right = len(nums)-1

    # We need to accont for if the target will go beyond the array's current length.
    if target > nums[right]:
        return right+1

    while left < right:
        mid = (right - left) // 2 + left
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid+1
        else:  # If nums[mid] == target
            return mid

    return left


print(searchInsert([1, 3, 5, 6], 0))
