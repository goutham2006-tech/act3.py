def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

# Test Cases
print("Test 1:", merge([[1,3],[2,6],[8,10],[15,18]]))   # Expected: [[1,6],[8,10],[15,18]]
print("Test 2:", merge([[1,4],[4,5]]))                   # Expected: [[1,5]]
print("Test 3:", merge([[4,7],[1,4]]))                   # Expected: [[1,7]]
