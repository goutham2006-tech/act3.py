def sortArray(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left  = sortArray(nums[:mid])
    right = sortArray(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test Cases
print("Test 1:", sortArray([5,2,3,1]))        # Expected: [1,2,3,5]
print("Test 2:", sortArray([5,1,1,2,0,0]))    # Expected: [0,0,1,1,2,5]
