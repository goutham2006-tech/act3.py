import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (inverted)
        self.large = []  # min-heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

# Test Cases
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print("Test 1:", mf.findMedian())   # Expected: 1.5
mf.addNum(3)
print("Test 2:", mf.findMedian())   # Expected: 2.0
