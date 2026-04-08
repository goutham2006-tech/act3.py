def topKFrequent(nums, k):
    from collections import Counter
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

# Test Cases
print("Test 1:", topKFrequent([1,1,1,2,2,3], 2))          # Expected: [1,2]
print("Test 2:", topKFrequent([1], 1))                      # Expected: [1]
print("Test 3:", topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))  # Expected: [1,2]
