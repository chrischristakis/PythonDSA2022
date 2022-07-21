#REVERSE A STRING
def p1s1(str):
    # Time complexity: O(n)
    # Space complexity: O(n)
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev += str[i]
    return rev


def p1s2(str):
    # Time complexity: O(n)
    # Space complexity: O(n)
    return str[::-1]


# MERGE SORTED ARRAYS
def p2s1(a1, a2):
    # Time complexity: O(a+b)
    # Space complexity: O(a+b)
    newArr = []
    i = j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            newArr.append(a1[i])
            i += 1
        else:
            newArr.append(a2[j])
            j += 1

    # Only one will have leftovers, add those.
    newArr = newArr + a1[i:] + a2[j:]
    return newArr


def twoSum1(nums, target):
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


def twoSum2(nums, target):
    map = {}
    for i in range(0, len(nums)):
        diff = target-nums[i]
        if nums[i] in map:
            return [i, map[nums[i]]]
        map[diff] = i


# Wayyy too slow!
def maxSubArray1(nums):
    # Time complexity O(n^2)
    max_sum = float('-inf')
    for i in range(0, len(nums)):
        local_sum = 0
        for j in range(i, len(nums)):
            local_sum += nums[j]
            max_sum = max(local_sum, max_sum)
    return max_sum

# Kadanes algorithim O(n)!!
def maxSubArray2(nums):
    # Basically, at any nums[i], if we knew what the greatest sum so far before nums[i] was, so max_sum[i-1], then
    # The largest sum will either max(nums[i], nums[i]+max_sum[i-1]). We then compare this to our global max_sum, and
    # Store the largest result.

    global_max = float('-inf')
    curr_max = 0
    for num in nums:
        curr_max = max(num, num + curr_max)
        global_max = max(curr_max, global_max)
    return global_max


str = "Hi I'm Chris"
print(p1s1(str))
print(p1s2(str))
a1 = [1, 2, 4, 6, 7, 8, 9]
a2 = [0, 3, 5]
print(p2s1(a1, a2))

nums = [2, 7, 11, 15]
print(twoSum1(nums, 9))
print(twoSum2(nums, 9))

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray1(nums))
print(maxSubArray2(nums))