import heapq

class KthLargestRunningStream:
    def __init__(self, data, k):
        self.min_heap = data
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val : int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k :
            heapq.heappop(self.min_heap)
        return self.min_heap

    def kSmallest(self, val : int) -> int:
        return heapq.nsmallest(self.k, self.min_heap)

if __name__ == "__main__":
    kth = KthLargestRunningStream([1,2,3,5,8,9], 3)
    result = kth.add(10)
    print(result)

    print(kth.kSmallest(3))








